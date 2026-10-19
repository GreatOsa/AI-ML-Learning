# there are 4 bitwise operator which are and, or, xor and not

import cv2 as cv 
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rectange = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle', rectange)
cv.imshow('Circle', circle)

# bitwise AND
bitwise_nd = cv.bitwise_and(rectange,circle)
cv.imshow('Bitwise_And', bitwise_nd)

#bitwise nor
bitwise_or = cv.bitwise_or(rectange,circle)


# Bitwise xor
bitwise_xor = cv.bitwise_xor(rectange,circle)
cv.imshow('Bitwise xor', bitwise_xor)

# Bitwise not
bitwise_not = cv.bitwise_not(rectange,circle)
cv.imshow('Bitwise not', bitwise_not)

cv.waitKey(0) 
