import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('lena.jpg', -1)
cv.imshow('image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()



cv.waitKey(0)
cv.destroyAllWindows()



#Using matplotlib you can include multiple images in one window.