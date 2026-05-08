import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale) # It means it's a quarter smaller
    height=int(frame.shape[0]*scale) # Frame.shape[0]:means height
    # Python understands length first,then width,so we set 1 for width and 0 for length.
    dimensions=(width,height) # New sizes
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) # To fill in the gaps when the image is resized so that it appears clear and without distortion.
capture=cv.VideoCapture('ai/cake.mp4')
while True:
    isTrue,frame=capture.read() # The program pulls one farme from the video each time the episode plays.
    if isTrue:
        frame_resized=rescaleFrame(frame,scale=0.5)
        cv.imshow('habibti',frame)
        cv.imshow('video resized',frame_resized)
    else:
        break
    if cv.waitKey(20)&0xFF==ord('d'): # So the video doesn't disappear at lightning speed., if i press the letter d on your keyboard,close the program.
        break
capture.release() # So that the device does not freeze or keep consuming RAM.
cv.destroyAllWindows()
