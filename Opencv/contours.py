# Contours are the boundaries of objects in an image. They are curves or lines that connect continuous points along the boundary of an object.

import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# canny = cv.Canny(img,125,175)
# cv.imshow('Canny edge',canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow(' Tresh',thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.drawContours(blank,contours,-1, (0,0,255),1)
cv.imshow('Contours Drawn', blank )




cv.waitKey(0)