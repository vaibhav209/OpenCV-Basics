import cv2 as cv

# Kernal Size = no. column by no. of rows


img = cv.imread('bird.jpg')
cv.imshow("Image", img)


# Averaging Method

avg = cv.blur(img, (3,3))
cv.imshow("avg_img", avg)

# Gaussian Blur

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gauss", gauss)


# Median Blurr

med = cv.medianBlur(img, (3))
cv.imshow("Median", med)

# Bilateral Blurr

bilat = cv.bilateralFilter(img, 20, 20, 5)
cv.imshow("bilateral", bilat)

cv.waitKey(0)
cv.destroyAllWindows()