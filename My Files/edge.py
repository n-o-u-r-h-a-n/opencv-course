import cv2 as cv 
import numpy as np

img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

#2 other ways to compute gradients/edges other than canny method :

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Edge Cascade (Gets the edges in an image wowwww)
canny = cv.Canny(img, 125 , 175) #fewer edges when we pass the blurred image 
cv.imshow('Canny Edges',canny)

#Laplacian Method : like a pencil shading of the image
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel Method :
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)#last 2 parameters are x-direction and y-direction respectively 
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel y',sobely)
cv.imshow('Combined Sobel',combined_sobel)

#Face Detection is detecting the face is present in an image or not while Face Recognition tells us who is this face for 
#Face Detection is done using a classifier(har cascade) which says whether the image is +ve or -ve 
#

cv.waitKey(0)
