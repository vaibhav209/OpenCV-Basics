import cv2 as cv
import numpy as np

#Merge the two images

img = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo.png')    

print(img.shape)               #Number of rows, columns and channels
print(img.size)                #Total number of pixel
print(img.dtype)               #Image dtatype is obtained
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

#ROI - Region of Interest
#you can copy any image from the image window

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

img = cv.resize(img, (512,512))
img2 = cv.resize(img2, (512,512))


# dst = cv.add(img,img2)
dst = cv.addWeighted(img, 1, img2, 2, 0)


cv.imshow("Image", dst)

cv.waitKey(0)
cv.destroyAllWindows()