import cv2 as cv 

# 1--> Reading Images :
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#Reading Videos :
capture = cv.VideoCapture('Videos/dog.mp4') #0 references your webcam 1 your 1st camera , etc or provide a path  

#Reading the video frame by frame : 
while True:
    isTrue, frame = capture.read() #reads the frame and a boolean which says the frame was successfully been read or not 
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame) # to display
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):#to prevent video from playing indefinitely
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0) #waits for a key to be pressed 

#-----------------------------------------------------------------------
# 2--> Resizing and Rescaling : 
def rescaleFrame(frame, scale=0.75):  #works with images,videos,live videos
    width = int(frame.shape[1] * scale)  #frame.shape[1] actually gets the width
    height = int(frame.shape[0] * scale)  
    dimensions = (width,height)  #tuple created

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):#works with live videos only 
    capture.set(3,width)
    capture.set(4,height)






