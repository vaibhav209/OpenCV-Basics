# import cv2 as cv
# import numpy as np


# img = cv.imread('gradient.png',0)
# _, th1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
# _, th2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
# _, th3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
# _, th4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
# _, th5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)


# cv.imshow("Image", img)
# cv.imshow("Thresh1", th1)
# cv.imshow("Thresh2", th2)
# cv.imshow("Thresh3", th3)
# cv.imshow("Thresh4", th4)
# cv.imshow("Thresh5", th5)



# cv.waitKey(0)
# cv.destroyAllWindows()


 

#####   Adaptive Threshold Method   #####

import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',0)
_, th1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("Image", img)
cv.imshow("thrsh1", th1)
cv.imshow("thrsh2", th2)
cv.imshow("thrsh3", th3)


cv.waitKey(0)
cv.destroyAllWindows()