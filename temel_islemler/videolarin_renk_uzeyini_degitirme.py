import cv2

cap = cv2.VideoCapture(
    "Güllü - Sabah Olmadan _ Boom Bap Beat _ Cem Yılmaz [Prod.by KaanHami].mp4")

while True:
    ret, frame = cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', frame)
    if ret == 0:
        break
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
