# Display and Save videos using Camera 

import cv2 as cv
cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(0) & 0xFF == ord('q'):           #0XFF is mask provide for 64bit device
        break

cap.release()
cv.destroyAllWindows()
