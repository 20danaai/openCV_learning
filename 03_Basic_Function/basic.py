import cv2 as cv
import numpy as np
img=cv.imread('photo3.jpg')
cv.imshow('nice',img)
# Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
# Edge cascade
canny=cv.Canny(img,200,600)
canny=cv.Canny(blur,50,200) # 200: The upper threshold , any edge higher than which the program draws ,
# 50: The lowest threshold , any edge least strength , will be ignoredcv.imshow('canny',canny)
# Dilating the imag
dilated=cv.dilate(canny,(7,7),iterations=3) # Wide brush(7,7), iterations: repeat the process 3 times consecutively
cv.imshow('Dilated',dilated)
# Eroding 
eroder=cv.erode(dilated,(7,7),iterations=1) # To reduce the thickness of the edges and sculpt them
cv.imshow('Eroder',eroder)
# Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) # Width first, then length
cv.imshow('Resize',resized)
# Cropped
cropped=img[400:800,400:800] # [y_start:y_end,x_start:x_end]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
