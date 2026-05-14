img=cv.imread('dogs.jpg')
cv.imshow('Img',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# Laplaction
lap=cv.Laplacian(gray,cv.CV_64F) # cv_64: High precision data tybe
lap=np.uint8(np.absolute(lap)) # np.absolute converts all negative num to positive,and np.uint8 returns them to img formate(0-255) 
cv.imshow('Laplaction',lap)
# Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0) # The spaces between right and left.
sobely=cv.Sobel(gray,cv.CV_64F,0,1) # The spaces between above abd below.
combiened_sobel=cv.bitwise_or(sobelx,sobely) # To collect edges.
cv.imshow('SobelX',sobelx)
cv.imshow('SobelY',sobely)
cv.imshow('Combiened_Sobel',combiened_sobel)
# Canny
canny=cv.Canny(gray,50,105) # Professional and clean detection,the most commonly used.
cv.imshow('Canny',canny)
cv.waitKey(0)
