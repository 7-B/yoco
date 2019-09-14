import torch
from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua

from PIL import Image

# Check prcess time
import time 
import cv2
highThresh	= 0.4
lowThresh	= 0.1

def sobel (img):
	'''
	Detects edges using sobel kernel
	'''
	opImgx		= cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)	#detects horizontal edges
	opImgy		= cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)	#detects vertical edges
	#combine both edges
	return cv2.bitwise_or(opImgx,opImgy)	#does a bitwise OR of pixel values at each pixel

def sketch(path):	
   #loat image
   frame = cv2.imread(path,0)
   #Blur it to remove noise
   frame		= cv2.GaussianBlur(frame,(3,3),0)

   #make a negative image
   invImg	= 255-frame

   #Detect edges from the input image and its negative
   edgImg0		= sobel(frame)
   edgImg1		= sobel(invImg)
   edgImg		= cv2.addWeighted(edgImg0,1,edgImg1,1,0)	#different weights can be tried too

   #Invert the image back
   opImg = 255-edgImg
   return opImg


def simplify(np_array):
   t0 = time.time()

   use_cuda = torch.cuda.device_count() > 0

   cache  = load_lua('model_gan.t7')
   model  = cache.model
   immean = cache.mean
   imstd  = cache.std
   model.evaluate()

   #data  = Image.open(path).convert('L')
   data = Image.fromarray(np_array)
   w, h  = data.size[0], data.size[1]
   pw    = 8-(w%8) if w%8!=0 else 0
   ph    = 8-(h%8) if h%8!=0 else 0
   data  = ((transforms.ToTensor()(data)-immean)/imstd).unsqueeze(0)
   if pw!=0 or ph!=0:
      data = torch.nn.ReplicationPad2d( (0,pw,0,ph) )( data ).data

   if use_cuda:
      print("PyTorch is using CUDA")
      print("CUDA device count :",torch.cuda.device_count())
      print("GPU :",torch.cuda.get_device_name(0))
      pred = model.cuda().forward( data.cuda() ).float()
   else:
      pred = model.forward(data)
   save_image(pred[0],'static/output/out.png')
   t1 = time.time()
   total = t1-t0
   print(total,"sec spent")

def convert_to_line(filename):
    path = "static/input/"
    filename = path + filename
    sketch_npArray = sketch(filename)
    simplify(sketch_npArray) #create out.png in current directory

def toSVG(): #Implement later
   pass

#convert_to_line('test.jpg')