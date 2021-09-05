import cv2 as cv 

cap = cv.VideoCapture('car.avi')

while cap.isOpened():
    _, img = cap.read()

    img = cv.resize(img, (600, 400))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('GRAY', gray)

    car_cascade = cv.CascadeClassifier('haar_cars.xml')

    car_rect = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)


    for (x, y, w, h) in car_rect:
        cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), thickness=2)

    #Display the immage
    cv.imshow("Detected", img)
    
    if cv.waitKey(33) == 27 :
        break

cap.release()
cv.destroyAllWindows()