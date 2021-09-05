import cv2 as cv
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv.imread("bit.png")
 
#Bitwise AND Operator
bitAnd = cv.bitwise_and(img2, img1)
#OR Operator
bitOR = cv.bitwise_or(img2, img1)
#XOR Operator
bitXOR = cv.bitwise_xor(img2, img1)\
#NOT Operator
bitNot1 = cv.bitwise_not(img1)
bitNot2 = cv.bitwise_not(img2)



cv.imshow("image1", img1)
cv.imshow("image2", img2)
cv.imshow('BitAnd', bitAnd)
cv.waitKey(0)
cv.destroyAllWindows()