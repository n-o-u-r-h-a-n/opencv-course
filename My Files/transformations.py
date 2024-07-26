import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

#Translation -ve x --> left and vice versa + -ve y up and vice versa
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

translated = translate(img, -100, 100)
cv.imshow('Translated',translated)

#Rotation 
def rotate(img , angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width,height)

    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img,-45)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated,-45)
cv.imshow('Rotated Twice',rotated_rotated)

#To avoid excess triangles do not rotate twice , rotate on;y 1 time with -90

#Resizing : (same as before)
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)#when resizing to smaller dimentions if large dimentions use _LINEAR OR _CUBIC (Cubic is the slowest one among the 3 but produces the highest quality one) 
cv.imshow('Resized',resize)

#Flipping :
flip = cv.flip(img,1)#2nd parameter is flip code...it could be either 0,1 or -1 where 0 indicates flipping the image vertically over the x-axis, 1 flipping horizontally over the y-axis, and -1 flips the image both vertically and horizontally 
cv.imshow('Flipped',flip) 

#Cropping : (same as before)
cropped = img[50:200 , 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)