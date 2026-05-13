import cv2 as cv
img=cv.imread('jennie.jpg')
cv.imshow('img',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# Simple thresholding
threshold,thresh=cv.threshold(gray,155,255,cv.THRESH_BINARY) # 255: means white
# Any pixel with a value greater than 155 becomes white,and any pixel smaller becomes black(to isolate the dark parts from the light ones).
cv.imshow('Simple Thresholded',thresh)
threshold,thresh_inv=cv.threshold(gray,155,255,cv.THRESH_BINARY_INV) # Completely opposite above.
cv.imshow('Simple Thresholded Inverse',thresh_inv)
# Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,21,5) # 11: Exclusively single , 3: It helps clean the image of noise.
# Instead of using a single number (like 155) for the entire image, the computer takes each small area in the image and calculates its own "threshold" based on its neighbors (the surrounding areas).
cv.imshow('Adaptive Thresholding',adaptive_thresh)
cv.waitKey(0)
