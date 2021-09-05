########## RGB (COLORED_IMAGE) TO BINARY  ##########
 
# In an original image the data is very complex so that the noumber of RED_GREEN_BLUE(RGB) layer are present on one image 

# First we have to change the original image to gray scale image that is easy to deal with image by converting it into Binary form

# Now we have use a threshold technique

# That you can choose any random point i.e. value

# From that value you can show some black point under that value & White point over that value



import cv2
img = cv2.imread('sample.jpg',0)
cv2.imshow("Gray", img)

cv2.waitKey(0)

ret, bw = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Image", bw)


cv2.waitKey(0)
cv2.destroyAllWindows(0)