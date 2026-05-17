import os
import numpy as np
import cv2 as cv
people=['Rodrigo De Paul','Lionel Messi', 'Cristiano Ronaldo']
DIR=r'C:\Users\PT\Desktop\faces_train'
haar_cascade=cv.CascadeClassifier(r'C:\Users\PT\Desktop\hello\ai\Section #3 - Faces\haar_face.xml')
features=[] # Facial features
labels=[] # People numbers
def creat_train():
    for person in people: # Go through the list of people's names
        path=os.path.join(DIR,person) # We specify the folder path for each person
        label=people.index(person) # This line takes the person's index in the list and converts it to a number.
    for img in os.listdir(path): # GO through the pictures inside it , one by one.
        img_path=os.path.join(path,img) # We merge the person's folder path with the current image name.
        img_arry=cv.imread(img_path)
        gray=cv.cvtColor(img_arry,cv.COLOR_BGR2GRAY)
        faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1) # It crops out the face and ignores the background.
        for(x,y,w,h) in faces_rect:
            faces_roi=gray[y:y+h,x:x+w] # Region of interest
            features.append(faces_roi) # WEtake the face crop we cut out(face_roi) and add it to a large list called features, which is what the ai will learn.
            labels.append(label)
creat_train()

features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer=cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels) # Training moment

face_recognizer.save('face_trained.yml') # Save to an external file on your computer.
np.save('features.npy',features)
np.save('labels.npy',labels)
