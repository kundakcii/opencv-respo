import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8)+255

# thickness kalınlığı gösterir
cv2.line(canvas, (50, 50), (512, 512), (255, 0, 0), thickness=5)
cv2.line(canvas, (100, 50), (200, 250), (0, 0,255), thickness=7)

cv2.imshow("canvas", canvas)


cv2.waitKey(0)
cv2.destroyAllWindows()
