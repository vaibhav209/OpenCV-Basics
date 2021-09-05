
#Contours is usefull in edge analysis, object detection and Face recognition

#Contours is basically the boundry of object
#The line or curve that joins the continious points of object
#Each individual contour is a numpy array of (x,y) of boundry points of the object



import cv2 as cv
import numpy as np


img = cv.imread('download.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 127, 255, 0)

contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print("Number of contours = " + str(len(contours)))
print(contours[0])



cv.drawContours(img, contours, 11, (0,255,0), 3)




cv.imshow("Image", img)
cv.imshow("Gray", gray)
cv.waitKey(0)
cv.destroyAllWindows()