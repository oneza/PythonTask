# Поиск синего маркера на видеопотоке с веб-камеры

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([40, 90, 0])
    upper_blue = np.array([120, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel=np.ones((5,5),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    mask=cv2.dilate(mask,kernel,iterations=1)

    contours, _ = cv2.findContours(mask, 1, 2)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        cv2.drawContours(frame,[box],0,(0,0,255),2)
        cv2.drawContours(mask,[box],0,(0,0,255),2)

    concat =  np.concatenate((frame, mask), axis=1)
    cv2.imshow("Task1", concat)

    key = cv2.waitKey(25)
    if key == 27:
        break
        
cap.release()
cv2.destroyAllWindows()