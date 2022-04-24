import cv2
import numpy as np

img1 = cv2.imread("text.png")
img2 = cv2.imread("contour.png")


gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray1=np.float32(gray1)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray2=np.float32(gray2)

corners1 =cv2.goodFeaturesToTrack(gray1,500,0.01,10)
corners2 =cv2.goodFeaturesToTrack(gray2,100,0.01,10)

corners1 =np.int0(corners1)
corners2 =np.int0(corners2)

for corner in corners1:
    x,y =corner.ravel()
    cv2.circle(img1,(x,y),3,(0,0,255),-1)

for corner in corners2:
    x,y =corner.ravel()
    cv2.circle(img2,(x,y),3,(0,0,255),-1)

cv2.imshow("corner1",img1)
cv2.imshow("corner2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()  