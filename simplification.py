import torch
from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua

from PIL import Image

def simplify():
   use_cuda = torch.cuda.device_count() > 0

   cache  = load_lua('model_gan.t7')
   model  = cache.model
   immean = cache.mean
   imstd  = cache.std
   model.evaluate()

   data  = Image.open('sketchKeras.jpg').convert('L')
   w, h  = data.size[0], data.size[1]
   pw    = 8-(w%8) if w%8!=0 else 0
   ph    = 8-(h%8) if h%8!=0 else 0
   data  = ((transforms.ToTensor()(data)-immean)/imstd).unsqueeze(0)
   if pw!=0 or ph!=0:
      data = torch.nn.ReplicationPad2d( (0,pw,0,ph) )( data ).data

   if use_cuda:
      pred = model.cuda().forward( data.cuda() ).float()
   else:
      pred = model.forward(data)
   save_image( pred[0], 'out.png')