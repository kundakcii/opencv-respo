from curses.panel import bottom_panel
import cv2
import numpy as np
import math


def findMaxContours(contours):
    max_i = 0
    max_area = 0
    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])
        if max_area < area_face:
            max_area = area_face
            max_i = i
        try:
            c = contours[max_i]
        except:
            contours = [0]
            c = contours[0]
        return c


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    roi = frame[50:250, 200:400]  # frame[y1:y2,x1:x2]
    cv2.rectangle(frame, (200, 50), (400, 250), (0, 0, 255), 0)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 45, 79], dtype=np.uint8)
    upper_color = np.array([17, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones([3, 3], dtype=np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.medianBlur(mask, 15)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        try:
            c = findMaxContours(contours)
            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            extBottom = tuple(c[c[:, :, 1].argmax()][0])

            cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)
            cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
            cv2.circle(roi, extTop, 5, (0, 255, 0), 2)
            cv2.circle(roi, extBottom, 5, (0, 255, 0), 2)

            cv2.line(roi, extLeft, extTop, (255, 0, 0), 2)
            cv2.line(roi, extTop, extRight, (255, 0, 0), 2)
            cv2.line(roi, extRight, extBottom, (255, 0, 0), 2)
            cv2.line(roi, extBottom, extLeft, (255, 0, 0), 2)

            a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1]))
            b = math.sqrt((extBottom[0]-extRight[0]) **
                          2+(extBottom[1]-extRight[1]))
            c = math.sqrt((extBottom[0]-extTop[0])**2+(extBottom[1]-extTop[1]))
            try:
                angle_ab = int(math.acos((a**2+b**2-c**2)/(a*b*c))*57)
                cv2.putText(roi, str(angle_ab), (extRight[0]-10, extRight[1]),
                            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1, (0, 0, 255), 2, cv2.LINE_AA)
            except:
                cv2.putText(roi, "?", (extRight[0]-50, extRight[1]),
                    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,4, (0, 0, 255), 2, cv2.LINE_AA)
        except:
            print("hata")
    cv2.imshow("frame", frame)
    cv2.imshow("roi", roi)
    cv2.imshow("mask", mask)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
