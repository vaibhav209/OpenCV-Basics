import cv2 as cv 

img = cv.imread('lena.jpg', 1)

cv.imshow("Alpha", img)

cv.waitKey(0)
cv.destroyAllWindows()

# Write the original image in another file
cv.imwrite('lena_copy.png', img)









#Flag for Read Image

# 1 for color image
# 0 for GrayScale Mode
# -1 Loads image as such including alpha channel