# import numpy as np
# import cv2 as cv 

# # events = [i for i in dir(cv) if 'EVENT' in i]
# # print(events)


# def click_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         print(x, ', ', y)
#         font = cv.FONT_HERSHEY_SIMPLEX
#         strXY = str() + 'This is MouseEvent'+ str()
#         cv.putText(img, strXY, (x,y), font, 1,(255,255,0),2)
#         cv.imshow('Image', img)

# img = np.zeros((512,512,3), np.uint8)
# cv.imshow('Image', img)

# cv.setMouseCallback('Image', click_event)

# cv.waitKey(0)
# cv.destroyAllWindows()




# Click to draw 2 or more point to create lines


import numpy as np
import cv2 as cv 


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv.rectangle(img, points[-1], points[-2], (255,0,0), 5)
        cv.imshow('Image', img)

img = np.zeros((512,512,3), np.uint8)

cv.imshow('Image', img)


points = []
cv.setMouseCallback('Image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()