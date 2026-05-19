import cv2 as cv

cap = cv.VideoCapture(0)
haar_cascade=cv.CascadeClassifier(r'C:\Users\PT\Desktop\hello\ai\Section #3 - Faces\haar_face.xml')
while True:
    ret, frame = cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    face_react=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)
    for (x,y,w,h) in face_react:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),thickness=4)
        cv.putText(frame,'Dania',(x,y),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
    

    cv.imshow("Camera", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
