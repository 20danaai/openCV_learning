import cv2 as cv
cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    blurred_frame=cv.blur(frame,(35,35))
    cv.imshow('Camera',blurred_frame)
    if cv.waitKey(1)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
