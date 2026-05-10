import cv2 as cv
import numpy as np
img=cv.imread('girl.jpg')
cv.imshow('img',img)
b,g,r=cv.split(img) # Image splitting process into thirds : blue, green, red matrix
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
print(img.shape) # (height,width,channels)
print(b.shape) # Each color channels maintains the same size as the original image.
print(g.shape)
print(r.shape)
merged=cv.merge([b,g,r]) # Restoration of separate color channels
# merged=cv.merge([r,g,b]) # change colors
cv.imshow('merged',merged)
blank=np.zeros(img.shape[:2],dtype='uint8') # Creat an array of zeros and merge it with only one channel to view the image in only one color
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,b,blank])
red=cv.merge([blank,blank,b])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
cv.waitKey(0)
