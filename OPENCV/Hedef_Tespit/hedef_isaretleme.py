import cv2
import numpy as np

camera = cv2.VideoCapture(0)
while True:
    ret, resim = camera.read()
    if not ret:
        break
    yukseklik, genislik = resim.shape[:2]
    hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    alt_red = np.array([0, 120, 70])
    ust_red = np.array([10, 255, 255])
    maske = cv2.inRange(hsv, alt_red, ust_red)
    kontourlar, hiyerarsi = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for knt in kontourlar:
        alan = cv2.contourArea(knt)
        if alan > 500:
            x, y, w, h = cv2.boundingRect(knt)
            cv2.rectangle(resim, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(resim, "Hedef", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            hedef_merkez_x = x + w // 2
            hedef_merkez_y = y + h // 2
            cv2.line(resim, (genislik // 2, yukseklik // 2), (hedef_merkez_x, hedef_merkez_y), (255, 0, 0), 2)
            Hata_X = hedef_merkez_x - genislik // 2
            Hata_Y = hedef_merkez_y - yukseklik // 2
            cv2.putText(resim, f"Hata X: {Hata_X}", (10, yukseklik - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(resim, f"Hata Y: {Hata_Y}", (10, yukseklik - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.circle(resim,(genislik//2,yukseklik//2),30,(0,0,255),3)
            if Hata_X > -40 and Hata_X < 40 and Hata_Y > -40 and Hata_Y < 40:
                cv2.putText(resim, "Hedefe kitlenildi ates etmeye hazir", (10, yukseklik - 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255), 3)
                cv2.circle(resim, (genislik//2,yukseklik//2), 30, (0, 255, 0), 3)
    cv2.putText(resim,"SISTEM AKTIF",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
    cv2.circle(resim,(genislik//2,yukseklik//2),5,(255,0,255),3)
    cv2.imshow("Hedef Isaretleme", resim)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()