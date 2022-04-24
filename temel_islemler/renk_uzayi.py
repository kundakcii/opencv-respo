import cv2

img =cv2.imread('a.jpg')

img_rgb =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('a rgb',img)
cv2.imshow('a bgr',img_rgb)
cv2.imshow('a rgb',img_hsv)
cv2.imshow('a gray',img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()