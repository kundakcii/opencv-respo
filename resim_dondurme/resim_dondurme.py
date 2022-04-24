import cv2
import numpy as np

img = cv2.imread('a.jpg',0)
row, col = img.shape
M1 = cv2.getRotationMatrix2D((col/2,row/2),90,3)
M2 = cv2.getRotationMatrix2D((col/2,row/2),180,1)
M3 = cv2.getRotationMatrix2D((col/2,row/2),270,1)

dst1 =cv2.warpAffine(img,M1,(col,row))
dst2 =cv2.warpAffine(img,M2,(col,row))
dst3 =cv2.warpAffine(img,M3,(col,row))

cv2.imshow('orjinal', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
