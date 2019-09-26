import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import math
import cv2

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
        r = math.ceil(height / float(h))
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = math.ceil(width / float(w))
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

mask = np.load("segment_output/original.npy")
img = cv2.imread("input/original.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
style_img = cv2.imread("style_transfer_image/style.png", cv2.IMREAD_COLOR)
style_img = cv2.cvtColor(style_img, cv2.COLOR_BGR2RGB)

print(type(img))

fig, axs = plt.subplots(1,5)

axs[0].imshow(img)
axs[1].imshow(mask)

cv2.imwrite("result/original_out.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

# 0:Background / 1:Hat / 2:Hair / 3:Glove / 4:Sunglasses 
# 5: Uppper-clothes / 6:Dress / 7:Coat / 8:Socks / 9:Pants 
# 10:Jumpsuits / 11:Scarf / 12:Skirt / 13:Face / 14:Left-arm
# 15:Right-arm / 16:Left-leg / 17:Right-leg / 18:Left-shoe / 19:Right-shoe

color_map = [1, 0, 0, 0, 0, 
             1, 0, 0, 0, 0, 
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0]


print("mask size: {}".format(mask.shape))
print("style size: {}".format(style_img.shape))

mask_size = mask.shape
img_size = img.shape


# style_img = cv2.resize(style_img, dsize=(mask_size[0], ma), interpolation=cv2.INTER_AREA)

# style_img = image_resize(style_img, height=mask_size[0], width=mask_size[1])

print("mask size: {}".format(mask.shape))
print("style size: {}".format(style_img.shape))

face = np.array(img, copy=True)

for row in range(mask_size[0]):
    for col in range(mask_size[1]):
        if color_map[mask[row][col]] == 1:
            face[row][col] = 0 
            img[row][col] = style_img[row][col]

style_img = cv2.cvtColor(style_img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

axs[2].imshow(style_img)
axs[3].imshow(img)
axs[4].imshow(face)

cv2.imwrite("result/styled_out.png", style_img)
cv2.imwrite("result/merge_out.png", img)
cv2.imwrite("result/face.png", face)

plt.show()
