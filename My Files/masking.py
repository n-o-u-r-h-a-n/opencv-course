import cv2 as cv
import numpy as np
#Masking : Focusing on specific parts of an image 

img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image',blank)

mask = cv.circle(blank,(img.shape[0]//2,img.shape[1]//2 +45), 100,255,-1)
cv.imshow('Mask',mask) #could make a rectangle as well or use both and and them to create a wierd shape which coul be used as a mask 

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)


cv.waitKey(0)
