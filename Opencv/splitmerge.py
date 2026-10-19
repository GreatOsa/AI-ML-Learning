import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
# cv.imshow('Park',img)

b,g,r = cv.split(img)


# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
 
#  note the upper code will show you in grayimage 

blank =np.zeros(img.shape[:2],dtype='uint8')

blue = cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red= cv.merge([blank,blank,r])

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

# to merge all to get the original image
merge = cv.merge([b,g,r])

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
cv.waitKey(0)