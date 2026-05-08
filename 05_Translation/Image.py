import cv2 as cv
import numpy as np
img=cv.imread('photo_2026-05-08_10-55-05.jpg')
cv.imshow('img',img)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]]) # Two_dimensional array.
    dimension=(img.shape[1],img.shape[0]) # (width,height).
    return cv.warpAffine(img,transMat,dimension) # This function is the one that actually performs the operation.
translated=translate(img,100,100)
# -x: left
# -y: up
# x: right
# y: down
cv.imshow('Translated',translated)
# Rotation
def rotate(img,angle,rotPoint=None): # The angle at which you want to rotate the image,The point around which the image will revolve by default
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2) #If i don't pass a rotation point when calling the function ,the image center is calculated.
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) #Rotation matrix , 1.0:Scale
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,100) # If i want to use a default value in the function , i write angle = 45
final_rotate=rotate(rotated,-400)
cv.imshow('Final_rotate',final_rotate)
cv.imshow('Rotated',rotated)
# Resize
resized=cv.resize(img,(100,400),cv.INTER_CUBIC)
# INTER_NEAREST : faster,lower quality,used in digital maps
# INTER_LINEAR : Medium speed,good quality,for shrinking
# INTER_CUBIC :Slow,excellent quality,enlarging
cv.imshow('Resize',resized)
# Flipping
flib=cv.flip(img,1)
flibing=cv.flip(img,0)
flibed=cv.flip(img,-1)
cv.imshow('Flipping',flibing)
cv.imshow('Fliped',flibed)
cv.imshow('Flip',flib)
cv.waitKey(0)
