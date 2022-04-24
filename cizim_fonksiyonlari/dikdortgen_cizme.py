import cv2
import numpy as np
canvas = np.zeros((512, 512, 3), np.uint8) + 255

# ilk olarak sol üst köşesi daha sonra sağ alt köşesi daha sonra rengi en sonda kalınlığı parametra olarak verilir.
# dikdörtgenin içini doldurmak istiyorsak kalınlık parametresini -1 olarak veririz.
cv2.rectangle(canvas, (20, 20), (50, 50), (0, 255, 0), thickness=-1)
cv2.rectangle(canvas, (200, 200), (40, 40), (0, 255, 0), thickness=2)
cv2.rectangle(canvas, (100, 100), (50, 50), (0, 255, 0), thickness=1)

cv2.imshow('canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
