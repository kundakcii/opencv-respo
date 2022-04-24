import numpy as np
import cv2
canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# ilk olarak merkez daha sonra (height,width) , yatay derece yaptığı açı,
# başlangıç ve bitiş açısı kaç dereceden başlayıp kaç dereceye kadar olacağı en son da kalınlığı
cv2.ellipse(canvas, (100, 400), (80, 20),0, 0, 360, (255, 255, 0),-1)
cv2.ellipse(canvas, (200, 300), (80, 20),50, 0, 360, (255, 255, 0),-1)
cv2.ellipse(canvas, (300, 300), (80, 20),90, 270, 360, (255, 255, 0),-1)
cv2.ellipse(canvas, (400, 300), (80, 20),130, 90, 360, (255, 255, 0),-1)
cv2.ellipse(canvas, (500, 300), (80, 20),180, 90, 360, (255, 255, 0),-1)

cv2.imshow('canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
