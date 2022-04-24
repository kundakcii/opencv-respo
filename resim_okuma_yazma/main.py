import cv2

img = cv2.imread("a.jpg")
#pencereyi yeniden boyutlandırmak için
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
print(img)

cv2.imshow("image", img)

#resimi kaydetmek
cv2.imwrite("deneme.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
