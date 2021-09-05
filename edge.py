import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#Edge Detection

# The canny edge detecttion is an edge detection operator
# that uses a multi-stage algorithm to detect a wide range of edges in image

#Canny edge detection algorithm is composed of 5 steps

# 1. Noise Reduction
# 2. Gradient Calculation
# 3. Non-maximum suppression
# 4. Double Threshold
# 5. Edge tracking by hysteresis


img = cv.imread('messi5.jpg')
cv.imshow("Image", img)

canny = cv.Canny(img, 100, 200)
cv.imshow("canny_image", canny)

cv.waitKey(0)
cv.destroyAllWindows()