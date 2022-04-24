import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255
# ilk olarak merkez daha sonra yarı çapı daha sonra rengi daha sonra kalınlığı
#daire yapmak için kalınlık -1 verilemeli
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=5)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
