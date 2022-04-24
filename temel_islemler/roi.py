import cv2
# roi bir resimde işlenecek kısmı tüm fotoğraftan ayırmaya yarar
img = cv2.imread("a.jpg")
#resmin boyutlarını alma
print(img.shape[:2])
#birincisi y ekseni ikincisi x ekseni
roi = img[30:200,200:370]

cv2.imshow('Klon', img)
cv2.imshow("ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
