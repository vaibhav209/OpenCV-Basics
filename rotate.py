# Image Rotation

import cv2 as cv

img = cv.imread('sample.jpg')
cv.imshow('Image', img)

height, width = img.shape[:2]

rotation_matrix = cv.getRotationMatrix2D((width/2, height/2),180,0.5)

rotated_image = cv.warpAffine(img, rotation_matrix, (width, height))

cv.imshow('Rotated Image', rotated_image)


# Transpose of Image : Rotate a image without any loss

import cv2 as cv

img = cv.imread('sample.jpg')
cv.imshow('Image', img)

rotate_img = cv.transpose(img) # Rotate at 90 degree

cv.imshow('Rotated', rotate_img)

cv.waitKey(0)
cv.destroyAllWindows()

