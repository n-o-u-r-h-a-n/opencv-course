import cv2 as cv
img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)
#IT WORKEDDD YAYYY!

#4 --> 5 Essential Functions (useful in any Computer Vision Project)
#Converting a BGR img to grayscale : 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blurring an image 
blur = cv.GaussianBlur(img, (15,15 ), cv.BORDER_DEFAULT) #2nd parameter is kernel size and should be an odd number 
cv.imshow('Blur',blur)

#Edge Cascade (Gets the edges in an image wowwww)
canny = cv.Canny(img, 125 , 175) #fewer edges when we pass the blurred image 
cv.imshow('Canny Edges',canny)

#Dilating the image (using the canny edges)
dilated = cv.dilate(canny, (14,14), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding (Get the dilated image back to the edge cascade version)
eroded = cv.erode(dilated, (14,14), iterations=3)
cv.imshow('Eroded',eroded)

#Resize 
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)#when resizing to smaller dimentions if large dimentions use _LINEAR OR _CUBIC (Cubic is the slowest one among the 3 but produces the highest quality one) 
cv.imshow('Resized',resize)

#Cropping (We can select a portion of the image on the basis of the pixel values)
cropped = img[50:200 , 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)