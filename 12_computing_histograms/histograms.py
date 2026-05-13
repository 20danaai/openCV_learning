import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
img=cv.imread('cakes.jpg')
cv.imshow('Img',img)
blank=np.zeros(img.shape[:2],dtype='uint8')

#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',mask)
# Grayscale Histograms
# gray_hist=cv.calcHist([img],[0],None,[256],[0,256]) # We put it in [] because the function can take more than one image at a time ) : because we have only have one channel
# Mask:the full image or just a specific part ,the degrees into which i want to divide the colors , limits of the color values you want to measure
# gray_hist=cv.calcHist([img],[0],mask,[256],[0,256])
# If the chart is pointing uowards to the left (close to 0) your image is dark.
# plt.figure()
# plt.title('Grayscale Histograms')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
# Colors Histograms
plt.figure()
plt.title(' Color Histograms')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    #hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)
