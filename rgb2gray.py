##### How to convert RGB to Gray Scale Image #####

import cv2

img = cv2.imread("sample.jpg")

cv2.imshow("original", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Scale Image", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


##### Another Techniques to show image in gray scale ########

import cv2

img = cv2.imread("sample.jpg", 0) #Flag_value = 0 (Gray_Scale_Image)

cv2.imshow("Gray Scale Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()

