import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

##Morphological Transformations
# 1. Dilation
# 2. Erosion
# 3. Opening
# 4. Closing
# 5. Morphological Gradient
# 6. Top Hat
# 7. Black Hat

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)

dilation = cv.dilate(mask, kernal, iterations = 2)

titles = ['image', 'mask', 'dilation']
images = [img, mask, dilation]

for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xtricks([]), plt.ytricks([])

plt.show()



