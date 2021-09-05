import cv2 as cv
import numpy as np

#Use trackbar whenever you want to change any value dynamically from image

def nothing(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('current', 'image', 0, 255, nothing)

 

switch = 'Color/Gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)



while(True):
    img = cv.imread('messi5.jpg')
    pos = cv.getTrackbarPos('current', 'image')
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break


    s = cv.getTrackbarPos(switch, 'image')



    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        img = cv.imshow('Image', img)



cv.destroyAllWindows()