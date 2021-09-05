import cv2 as cv
import numpy as np

# Image Gradient:
# directional change in the intensity of light (Intensity will change from one side to another)

# Canny edge detection also uses Image-Gradient to detect edge.

img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow("image", img)

# Laplacian Method
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# SobelX & SobelY Method

# In SobelX method the intensity of color will be change in verticle direction in image 

# In SobelY method the intensity of color will be change in horizontal direction in image


sobelx = np.Sobel (img, cv.CV_64F, 1, 0)         #In SobelX "x=1" & y=0
sobely = np.Sobel (img, cv.CV_64F, 0, 1)         #In SobelX "x=0" & y=1

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

 

cv.imshow("laplacian", lap)
cv.imshow("sobel", sobelx, sobely)

cv.waitKey(0)
cv.destroyAllWindows()