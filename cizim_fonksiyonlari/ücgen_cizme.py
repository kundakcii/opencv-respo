import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8)

p1 = (100,  200)
p2 = (50, 50)
p3 = (300.100)

cv2.line(canvas, (100,  200),(50, 50),  (255, 0, 0), thickness=5)
cv2.line(canvas, (50, 50), (300, 100), (255, 0, 0), thickness=5)
cv2.line(canvas, (100,  200), (300, 100), (255, 0, 0), thickness=5)


cv2.imshow('canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
