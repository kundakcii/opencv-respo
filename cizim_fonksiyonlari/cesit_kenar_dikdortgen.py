import cv2
import numpy as np
canvas = np.zeros((512, 512, 3), np.uint8) + 255

points = np.array(
    [[[110, 200], [330, 200], [290, 220], [100, 100]]], dtype=np.int32)

# şeklin kapalı olmasını istiyorsak True
cv2.polylines(canvas, [points], True, (0, 0, 100), 5)

cv2.imshow('canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
