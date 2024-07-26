import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
#features = np.load('features.npy', allow_pickle=True)
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'../Resources\Faces\val\elton_john/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Detect the face in the image :
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)

#Results were not always correct bcz we trained the recognizer on < 100 images
#At least we should have a 1000 images for each person 
#For the deep computer vision model , we will only use the open cv library to read an image and resize it to specific dimentions
#We should have a GPU to speed up the training process
#Candle a platform which offers free GPUs will be used
#Simpsons character data available on kaggle
#Create a notebook on kaggle,add data set, install pip both again caer and conero and choose gpu then start coding
#all images shoul be resized to same size first before being fed
#When creating the training data, it goes inside each one of the highest 10 which have the highest no of images and add their photos to the training set
#We will seperate the training set to feautures and labels as the training set consists now of 13,511 lists where inside each of these lists are 2 elements the actual array and the labels itself 
#Normalizing the data will make the computer learn the feautures faster
#The model will train itself on the training data and tests itself on the validation data where 20 percent will go to the validation set and the rest to the training set
#Image data generator will create new images from the existing images to introduce some randomness to the network
#Callbacks list will schedule the learning rate of the machine at specific intervals 
#We'll use open cv to test how good our model is 

