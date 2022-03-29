# Importing opencv for computer vision
import cv2

# Importing numpy for array/matrices functions
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# Flip the camera horizontally so that it does not show mirrored moves

# cv2.imshow('original', img)
# cv2.waitkey(0)


def get_contours(img):
    cont, hec = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in cont:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 500:
            cv2.drawContours(img_og, [cnt], 0, (0, 0, 255), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            obj_x = approx.ravel()[0]
            obj_y = approx.ravel()[1]
            # cv2.circle(img_og, (obj_x, obj_y), 5, (0, 255, 0), -1)


while True:
    global img_og
    success, img_og = cap.read()

    imgGray = cv2.cvtColor(img_og, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    get_contours(imgCanny)

    cv2.imshow('Original Video', img_og)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


def detect_squares():
    pass
