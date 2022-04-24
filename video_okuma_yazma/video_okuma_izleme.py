import cv2
# eğer web camdan okunacak parametre olarak 0 verilmeli
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(
    "Güllü - Sabah Olmadan _ Boom Bap Beat _ Cem Yılmaz [Prod.by KaanHami].mp4")
while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    # 1 girilirse her bir frame y eksenine göre tersini alır
    #frame = cv2.flip(frame,)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
