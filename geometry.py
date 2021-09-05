import cv2 as cv
import numpy as np

# img = cv.imread('lena.jpg', 1)


# Create image using numpy zeros method
img = np.zeros([500, 500,3], np.uint8)

# Draw a line on image
img = cv.line(img, (6,0), (210,230), (0,0,0), 6)
# draw a arrowed line on image
img = cv.arrowedLine(img, (0,0), (100,100), (255,255,255), 3)
 
# Draw a Rectangle
img = cv.rectangle(img, (300,300), (500,500), (0,0,255), 5)  #(thickness = -1 is filled rectangle)

# Draw a circle on image
img = cv.circle(img, (400, 400), 50, (255,0,0), -1)


# Put a Text on image
font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "Hello", (1,3), font, 4, (255,0,0), 5, cv.LINE_AA)

cv.imshow("Image", img)


cv.waitKey(0)
cv.destroyAllWindows()