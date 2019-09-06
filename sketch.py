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
	opImg				= 255-edgImg
	cv2.imwrite('sketch.jpg',opImg)
	return