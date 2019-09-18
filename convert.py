import torch
from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua
from GPUtil import showUtilization as gpu_usage
from PIL import Image

# Check prcess time
import time 
import cv2

# png2svg
# conda install -c bioconda potrace
import os

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def sobel (img):
	'''
	Detects edges using sobel kernel
	'''
	opImgx		= cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)	#detects horizontal edges
	opImgy		= cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)	#detects vertical edges
	#combine both edges
	return cv2.bitwise_or(opImgx,opImgy)	#does a bitwise OR of pixel values at each pixel

def sketch(path, imgname):	
   # Extract img basename without extesnsion (ex: test.png -> test)
   imgbasename = os.path.basename(imgname).split('.')[0]     
   #load image
   frame = cv2.imread(path,0)   
   # resize to prevent CUDA out of memory
   frame = image_resize(frame,height=512) 
   #Blur it to remove noise
   frame	= cv2.GaussianBlur(frame,(3,3),0)
   #make a negative image
   invImg = 255-frame
   #Detect edges from the input image and its negative
   edgImg0 = sobel(frame)
   edgImg1 = sobel(invImg)
   edgImg = cv2.addWeighted(edgImg0,1,edgImg1,1,0)	#different weights can be tried too
   #Invert the image back
   opImg = 255-edgImg
   return opImg, imgbasename


def png2svg(pngimg): 
   print(pngimg)
   pnmname = os.path.basename(pngimg).split(".")[0] + ".pnm"
   svgname = os.path.basename(pngimg).split(".")[0] + ".svg"
   os.system("convert %s %s" % (pngimg, pnmname))
   if not os.path.exists('static/output'):
      os.mkdir('static/output')
   svgname ='static/output/' + svgname
   os.system("potrace -s -o %s %s" % (svgname, pnmname))
   os.remove(pnmname)
   os.remove(pngimg)


def simplify(sketch_np_array, imgbasename):
   t0 = time.time()
   use_cuda = torch.cuda.device_count() > 0
   cache  = load_lua('model_gan.t7')
   model  = cache.model
   immean = cache.mean
   imstd  = cache.std
   model.evaluate()

   data = Image.fromarray(sketch_np_array)
   w, h  = data.size[0], data.size[1]
   pw    = 8-(w%8) if w%8!=0 else 0
   ph    = 8-(h%8) if h%8!=0 else 0
   data  = ((transforms.ToTensor()(data)-immean)/imstd).unsqueeze(0)
   if pw!=0 or ph!=0:
      data = torch.nn.ReplicationPad2d( (0,pw,0,ph) )( data ).data
   

   if use_cuda:
      print("CUDA device count :",torch.cuda.device_count())
      print("GPU :",torch.cuda.get_device_name(0))
      print('Initial GPU Usage')
      gpu_usage()
      #pred = model.cuda().forward(data.cuda()).float()
      pred = model.forward(data)
   else:
      pred = model.forward(data)
   
   print('GPU Usage after allocating a bunch of Tensors')
   gpu_usage()

   pngname = imgbasename + '.png'
   save_image(pred[0],pngname)
   
   # Not working
   print('GPU Usage after deleting the Tensors')
   gpu_usage()

   print('GPU Usage after emptying the cache')
   gpu_usage()
   
   png2svg(pngname)
   #svgConvert(pngname)
   t1 = time.time()
   total = t1-t0
   print(total,"sec spent")

def convert_to_line(imgname):
   if not os.path.exists('static/input'):
      os.mkdir('static/input')
   img_path = os.path.join('static/input', imgname)
   sketch_npArray, img_base_name = sketch(img_path, imgname)
   simplify(sketch_npArray, img_base_name) #create out.png in current directory
