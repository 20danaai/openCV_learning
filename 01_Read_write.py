import cv2 as cv
# Reading photo
image=cv.imread('Ellaf.jpg')
cv.imshow('Elafo',image)
cv.waitKey(0) # Without it , the program would open and close the image in a fraction of a second.
# Reading video
capture=cv.VideoCapture('video_ellaf.mp4')
while True:
    isTrue,frame=capture.read() # The program pulls one farme from the video each time the episode plays.
    cv.imshow('habibti',frame)
    if cv.waitKey(20)&0xFF==ord('d'): # So the video doesn't disappear at lightning speed., if i press the letter d on your keyboard,close the program.
        break
capture.release() # So that the device does not freeze or keep consuming RAM.
cv.destroyAllWindows()
