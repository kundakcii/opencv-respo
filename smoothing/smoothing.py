import cv2
import numpy as np


img_filder = cv2.imread("filter.png")
median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")


# sadece pozitif tek sayılar olabilir
blur = cv2.blur(img_filder, (11, 11))
blur2 = cv2.GaussianBlur(img_filder, (5, 5), cv2.BORDER_DEFAULT)


blur_m = cv2.medianBlur(median, 9)

blur_b = cv2.bilateralFilter(img_bilateral, 9, 75, 75)


cv2.imshow("orjinal", img_bilateral)
cv2.imshow("blur_b", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
