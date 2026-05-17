import numpy as np
import cv2 as cv
haar_cascade=cv.CascadeClassifier(r'C:\Users\PT\Desktop\hello\ai\Section #3 - Faces\haar_face.xml')
people=['Rodrigo De Paul','Lionel Messi', 'Cristiano Ronaldo']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml') 
img=cv.imread(r'c:\Users\PT\Desktop\faces_train\Cristiano Ronaldo\photo_2026-05-16_00-44-50.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.imshow('person',gray)
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)
for(x,y,w,h) in faces_rect:
            faces_roi=gray[y:y+h,x:x+w]
            label,confidence=face_recognizer.predict(faces_roi)
            print(f'labels = {people[label]} with the confidence {confidence}')
            cv.putText(img,str(people[label]),(x,y-40),cv.FONT_HERSHEY_DUPLEX,1.0,(0,0,0),thickness=3)
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected_face',img)
cv.waitKey(0)
# labels = Cristiano Ronaldo with the confidence 86.03449833681309
