import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#Histograms visualizes to us the distribution of pixel intensities in an image
img = cv.imread("C:/Users/nourh/OneDrive/Desktop/meee.jpg")
cv.imshow('Nourhan',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#Applying grayscale histogram on a masked image(portion of it)
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2), 100,255,-1)#before was circle

masked = cv.bitwise_and(img,img,mask=mask)#before was mask = (circle)
cv.imshow('Mask',masked)


#Grayscale Histogram
#gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256]) #where [256] is the no of bins of histogram and next parameter is the range of pixels 

#plt.figure()
#plt.title('GrayScale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#Colour Histogram 
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

#The mistake was using mask which was 3 channels to compute the histogram for one channel and this is not allowed in open cv so fixed it like above 

cv.waitKey(0)