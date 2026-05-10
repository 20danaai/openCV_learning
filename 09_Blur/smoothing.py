import cv2 as cv
img=cv.imread('img.jpg')
# Averaging
average=cv.blur(img,(7,7))
cv.imshow('Average_Blur',average)
# Gaussian Blur
gauss=cv.GaussianBlur(img,(9,9),0) # The numbers are exclusively odd , the best in terms of natural results
cv.imshow('Gauss_Blur',gauss)
# Median Blur
median=cv.medianBlur(img,7) # Salt and pepper
cv.imshow('Median_Blur',median)
# Bilateral
bilateral=cv.bilateralFilter(img,50,50,50) # soften the skin
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)
