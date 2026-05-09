import cv2 as cv
import numpy as np
img=cv.imread('contours2.jpg')
cv.imshow('img',img)
blank=np.zeros((1000,1000,3),dtype='uint8') 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
canny=cv.Canny(blur,50,100)
cv.imshow('Canny',canny)
ret,thresh=cv.threshold(gray,100,500,cv.THRESH_BINARY) # 100 : The lower the number,the darker the colors will be , and it will consider them as white
# 500 :Degree of whiteness.
cv.imshow('Thresh',thresh)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!') #688 contour(s) found!
# cv.RETR_EXTERNAL : it only brings you the extreme 'outer lines'.
# cv.RETR_LIST : it brings up all internal and external lines and is used to calculate the area.
# cv.RETR_CCOMP : it organizes the lines into only two levels.
# cv.RETR_TREE : Hierarchy , used to arrange shapes.
# CHAIN_APPROX_NONE : it stores 'all' the points on the line
# CHAIN_APPROX_SIMPLE : it provides a very large amount of memory space and is faster.
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours Drawn',blank)
cv.waitKey(0)
