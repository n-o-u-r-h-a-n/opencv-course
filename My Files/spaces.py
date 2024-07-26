import cv2 as cv 
import matplotlib.pyplot as plt


img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

plt.imshow(img)#Displays the image as if it is an RGB image not BGR 
plt.show()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Coverting the image to HSV :
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR to RGB 
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)#when passing the rgb it plots the bgr image 
plt.show()

#There is no way to convert from any type to another type, it should be converted to BGR itself

#HSV TO BGR :
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR',hsv_bgr)

#LAB TO BGR :
lab_bgr = cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow('LAB --> BGR',lab_bgr)


cv.waitKey(0)

