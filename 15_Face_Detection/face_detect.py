import cv2 as cv
img=cv.imread('ai/Resources/Photos/group 1.jpg')
cv.imshow('Group of 5 people',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade=cv.CascadeClassifier(r'C:\Users\PT\Desktop\hello\ai\Section #3 - Faces\haar_face.xml') # This line contains the AI file (trained algorithm) that recognizes the shape of a human face
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1) # 1.1: This means we reduce the img size by 10% each time.
print(f'Number of faces found ={len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected_face',img)
cv.waitKey(0)
