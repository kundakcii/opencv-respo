import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX


# metnin başlayacağı kordinat dol alt köşecen başlar
cv2.putText(canvas, "openCV", (30, 100), font1, 4, (0, 0, 0), cv2.LINE_AA)


cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
