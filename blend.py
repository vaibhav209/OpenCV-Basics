# Image Blending

# 1. Load the 2 images
# 2. find guassian pyramid of 2 images
# 3. From guassian pyramids find their laplacian pyramid
# 4. Now join the left half of apple and right half of orange in each leavel of laplacian pyramid
# 5. From joint image pyramid reconstruct the original image



import cv2 as cv 
import numpy as np

apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#Generate Gaussian Pyramid for img1-apple
apple_copy = apple.copy()





cv.imshow("Apple", apple)
cv.imshow("Orange", orange)
cv.imshow("blend-simply", apple_orange)
cv.waitKey(0)
cv.destroyAllWindows()


