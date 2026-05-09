import cv2 as cv
import matplotlib.pyplot as plt
img =cv.imread('color_photo.jpg')
cv.imshow('IMG',img)
# BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
# BGR to l*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)
# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(img)
#plt.imshow(rgb)
plt.show()
# HSV to BGR
hsv_BGR=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV__>BGR',hsv_BGR)
# LAB to BGR
lab_BGR=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB__>BGR',lab_BGR)
cv.waitKey(0)
