import cv2 as cv
import numpy as np


img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)


#Contours are the boundaries of the objects, different from edges,important tool in shape analysis and object detection and recognition 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# WAY 1 COUNTOURING :
#blur = cv.GaussianBlur(img, (15,15 ), cv.BORDER_DEFAULT) #2nd parameter is kernel size and should be an odd number 
#cv.imshow('Blur',blur)

#canny = cv.Canny(blur, 125 , 175) #fewer edges when we pass the blurred image 
#cv.imshow('Canny Edges',canny)


# WAY 2 CONTOURING :
#It basically looks at the image and try to binarize this image if below 125 the pixel will be set to black or 0 otherwise white or 1 
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#contours is a list of all coordinates of countours found in an image and hierarchies is the hierarchial representation of the contours
# RETR_EXTERNAL returns all external contours  and RETR_TREE returns all hierarchial contours 
# cv.CHAIN_APPROX_SIMPLE can compress all contours into simple ones that make sense,so compresses all points of a line into 2 endpoints only.
print(f' {len(contours)} contour(s) found!')
#After blurring, countours decreased from 327 to 18 ...using the threshold method it became 549


#We can visualize contours by drawing over the image 
cv.drawContours(blank,contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)




































cv.waitKey(0)