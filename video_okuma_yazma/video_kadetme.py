import cv2
cap = cv2.VideoCapture(0)

fileName = 'webcam.avi'
codec = cv2.VideoWriter_fourcc(c1='w', c2='M', c3='V', c4='2')
frameRate = 30
resolution = (640, 480)

videoFileOutPut = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()
    # 0 görüntüyü x eksenine göre çevirir -1 ise orjine göre çevirir
    frame = cv2.flip(frame, 1)
    videoFileOutPut.write(frame)
    cv2.imshow("Web Cam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


videoFileOutPut.release()
cap.release()
cv2.destroyAllWindows()
