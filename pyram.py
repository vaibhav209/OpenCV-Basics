##Image Pyramid

# Pyramid representation is type of multiscale signal type representation
# is a subject to repeated smoothing and subsampling

# Blur and sub-sample is increasing level by level

# Level 0
# Next level 1/2 (Resolution)
# Level 1/4 (Resolution)
# Level 1/8
# Level 1/16

# 1. Gaussian Pyramid
# 2. Laplacian Pyramid


import cv2 as cv 
import numpy as np

img = cv.imread('lena.jpg')
LR = cv.pyrDown(img)         #Shows the low resolution
LR2 = cv.pyrDown(LR)         #Shows the low resolution of LR

HR = cv.pyrUp(LR2)           #Shows the high resolution (Image showing little bit blurr)

cv.imshow("Image", img)
cv.imshow("Pyrdown 1", LR)
cv.imshow("Pyrdown 2", LR2)

cv.imshow("HighReso", HR)



cv.waitKey(0)
cv.destroyAllWindows()


# Laplacian Method

#Use of 'Laplacian Pyramid' & 'Guassian Pyramid'
 
# To blend the images and to Reconstruct the image

