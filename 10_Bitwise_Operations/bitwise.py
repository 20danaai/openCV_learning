import cv2 as cv
import numpy as np
blank=np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
# Bitwise AND
bitwise_and=cv.bitwise_and(rectangle,circle) # Intersection(only the common thing).
cv.imshow('Bitwise_And',bitwise_and)
# Bitwise OR
bitwise_or=cv.bitwise_or(rectangle,circle) # Bringing the two things together.
cv.imshow('Bitwise_OR',bitwise_or)
# Bitwise XOR
bitwise_xor=cv.bitwise_xor(rectangle,circle) # It only gives results in "non_common" areas.
cv.imshow('Bitwise_XOR',bitwise_xor)
# BItwise NOT
bitwise_not_rectangle=cv.bitwise_not(rectangle) # Reflecting colors
cv.imshow('Bitwise_NOT_rectangle',bitwise_not_rectangle)
bitwise_not_circle=cv.bitwise_not(circle)
cv.imshow('Bitwise_NOT_circle',bitwise_not_circle)
cv.waitKey(0)
