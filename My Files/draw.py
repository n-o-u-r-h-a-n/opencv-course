import cv2 as cv
import numpy as np

# 3--> Drawing Shapes and Putting Text : 

blank = np.zeros((500,500,3), dtype='uint8') #creating a blank image to draw on 
#3 parameters to be given are height,width,no of color channels 
cv.imshow('Blank', blank)

#Painting the image with a specific color
blank[:] = 0,255,0                 #if 0,0,255 will be red
cv.imshow('Green' ,blank)

#Coloring a specific portion of the image by giving range of pixels 
blank[200:300 , 300:400] = 0,255,0          
cv.imshow('Green' ,blank)

#Drawing a rectangle : 
cv.rectangle(blank, (0,0), (250,250), (0,255,0),thickness = 2) #thickness = cv.FILLED or to -1
cv.imshow('Rectangle' , blank) 

#Drawing a circle :
cv.circle(blank, (blank.shape[1]//2 , blank.shape[0]//2), 40, (0,255,0),thickness = 2) 
cv.imshow('Circle' , blank) 

#Drawing a line :
cv.line(blank, (0,0), (blank.shape[1]//2 , blank.shape[0]//2), (255,255,255), thickness = 3)
cv.imshow('Line',blank)

#Writing a text on the image : 
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX , 1.0, (0,255,0) , 2)
cv.imshow('Text' , blank)






img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

cv.waitKey(0)
