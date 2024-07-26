import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

#Splitting between color channels each img has 3 channels green, red and blue 
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])#setting green and red components to blank 
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)


#To visualize the shape of the image :#darker parts represent that this color is not present as much in that region
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)#shape has no 3 as it is only 1 channel that's why it is a gray-scaled image 
merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)

#Way to represent blue, green and red each with actual color not gray-scaled 


cv.waitKey(0)

