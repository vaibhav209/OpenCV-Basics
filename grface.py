import cv2 as cv

img = cv.imread('peoples.jpg')
cv.imshow('Group_Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

face_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(face_rect)}')


for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

#Display the immage
cv.imshow("Detected", img)


cv.waitKey(0)
cv.destroyAllWindows()