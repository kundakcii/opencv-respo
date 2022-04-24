import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("a.jpg", 0)


ret,th1 =cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th1 =cv2.threshold(img,150,200,cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7)


cv2.imshow('img', img)
cv2.imshow('imh th1', th1)
cv2.imshow('imh th2', th2)



cv2.waitKey(0)
cv2.destroyAllWindows()
