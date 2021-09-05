import cv2 as cv 
import numpy as np 

# This is incomplete code to perform Object Detection using HSV Color 

def nothing(x):
    pass

cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)

while(True):
    frame = cv.imread('smarties.png')

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])

    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask = mask)


    cv.imshow("Frame", frame)

    key = cv.waitKey(1)
    if key == 27:
        break


cv.destroyAllWindows()