import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#Thresholding is a binary realisation of the image ...cmp each pixel with this threshold value
#if less than threshold we set intensity to 0 otherwise we set it to 255 or white

img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple Thresholding :
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Threshold inv',thresh_inv)

#Adaptive Threshholding : Computer finds the optimal threshold value so value not given by the user 
adp_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)#last parameter is an integer subtracted from the mean to fine tune our measurement .....doing thresh_binary_inv makes all white parts black and vice versa....increasing value of last parameter while inv less white than how few the white was already  
cv.imshow('Adaptive Thresholding',adp_thresh)

#We can use gaussian method for thresholding instead where we add a weight for each pixel then get the mean across those pixels 


cv.waitKey(0)
