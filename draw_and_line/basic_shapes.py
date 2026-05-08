import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8') # Give me a matrix that is all zeros,
cv.imshow('blank',blank)
cv.imshow('Blank',blank) # Black
#  1. Paint the image a certain colour
blank[200:250,250:300]=(0,0,255)
cv.imshow('Blank',blank) # Red
# 2. Draw a rectangle
cv.rectangle(blank,(0,0),(250,500),(255,0,0),thickness=3)
cv.rectangle(blank,(0,0),(500,250),(255,0,0),thickness=-1)
cv.rectangle(blank,(blank.shape[1]//4,blank.shape[0]//4),((blank.shape[1]*3)//4,(blank.shape[0]*3)//4),(255,0,0),thickness=5)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]),(255,0,0),thickness=3)
cv.imshow('ractangle',blank)
# 3. Draw a circle
cv.circle(blank,(250,250),50,(250,250,250),thickness=2)
cv.imshow('circle',blank)
# 4. Draw a line 
cv.line(blank,(blank.shape[1]//4,blank.shape[0]//4),((blank.shape[1]*3)//4,(blank.shape[0]*3)//4),(250,250,0),thickness=4)
cv.imshow('line',blank)
# Write a text
cv.putText(blank,'hello i\'m Dania',(0,100),cv.FONT_HERSHEY_SIMPLEX,2,(0,250,250),thickness=3)
cv.imshow('text',blank)
cv.waitKey(0)
