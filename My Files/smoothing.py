import cv2 as cv 
#Smoothing and Blurring an image : 
#When there is a lot of noise from camera sensors which is basically problems in lighning 

img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

#Averaging : Creating a kernel window which makes pixel intensity of the middle square the average of pixel intensities of all other squares then this kernel window moves to the right and down to continue finshing the whole image
avg = cv.blur(img, (5,5))
cv.imshow('Average Blur',avg)

#Gaussian : Gets average of product of all weights where each square is given a specific weight, however it produces less blurring than Average method
gauss = cv.GaussianBlur(img, (5,5), 0)#the 3rd parameter is the standard deviation of the x-variable 
cv.imshow('Gaussian Blur',gauss)

#Median : gets the median of all other squares ...more effective blurring than averaging 
median = cv.medianBlur(img,5)#open cv understands 3 here as if is a tuple of 3 by 3
cv.imshow('Median Blur',median)

#Bilateral Bearing : the most effective one used in most advanced computer vision projects ...it takes care that edges are not removed 
bilateral = cv.bilateralFilter(img, 5, 15, 15)# 5 is the diameter size, 15 which is sigma space indicates that pixels at a specific distance will affect the pixel at the middle 
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)
