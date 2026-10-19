import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park',img)

# Translation
def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)
# cv.imshow("translated", translated)

# Rotation

def rotate(img,angle, rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint =(width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 180)
# cv.imshow("Rotated", rotated)

# resizing
resized = cv.resize(img,(500,500), interpolation = cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# Flipping
flip =cv.flip(img,-1) 
# 0 is to flip vertically, 1 is to to flip horizontally, and -1 is for both
# cv.imshow("flip",flip)

#Cropping
cropped = img[150:500,200:]
cv.imshow("Cropped", cropped)

cv.waitKey(0)