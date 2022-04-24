import cv2
img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

res, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

area = cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt, True)


cv2.imshow("orjinal", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
