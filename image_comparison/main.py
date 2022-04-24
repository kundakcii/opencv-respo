import cv2

img1 = cv2.imread("aircraft1.jpg")
img1 = cv2.resize(img1, (640, 550))

img2 = cv2.imread("aircraft1.jpg")
img2 = cv2.resize(img2, (640, 550))

if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")

diff = cv2.subtract(img1, img2)
b, g, r = cv2.split(diff)
print(b)
print(g)
print(r)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("same photo")
else:
    print("not same photo")

cv2.imshow("aircraft", img1)
cv2.imshow("aircraft", img2)
cv2.imshow("diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
