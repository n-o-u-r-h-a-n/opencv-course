import cv2 as cv 
import numpy as np
#Bitwise Operations : and,or,xor,not 
#A pixel is actually turned off when having a value of 0 and turned on when having a value of 1

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwise AND : Intersection of both --> white part
bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND',bit_and)

#Bitwise OR : Union of both --> white part as if both putted over each other
bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise AND',bit_or)

#Bitwise XOR : non-intersecting regions
#Bitwise OR minus Bitwise XOR gives Bitwise AND 
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_xor)
  
#Bitwise NOT : 
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT',bitwise_not)


cv.waitKey(0)


