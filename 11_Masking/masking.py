import cv2 as cv
import numpy as np
img=cv.imread('dogs.jpg')
cv.imshow('img',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
#mask=cv.rectangle(blank,(img.shape[1]//2-20,img.shape[0]//2-50),(img.shape[1]//2+100,img.shape[0]//2+100),255,-1)
# mask=cv.circle(blank,(img.shape[1]//2+50,img.shape[0]//2+30),100,255,-1)
# masked=cv.bitwise_and(img,img,mask=mask)
# cv.imshow('Masked image',masked)
rectangle=cv.rectangle(blank.copy(),(img.shape[1]//2,0),(img.shape[1],img.shape[0]),255,-1) # Mid_show to end(covers the entire right side)
cv.imshow('er',rectangle)
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1) # In center of the picture
werid_shape=cv.bitwise_and(rectangle,circle)
masked=cv.bitwise_and(img,img,mask=werid_shape) # Only the parts that are opposite the white color are visible
cv.imshow('werid shape masked image',masked)
cv.waitKey(0)
