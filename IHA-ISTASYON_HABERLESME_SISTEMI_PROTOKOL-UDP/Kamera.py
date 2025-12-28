from ultralytics import YOLO
import cv2
import socket
import time
socet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
model = YOLO("yolov8n.pt")
model.to("cpu")
kamera = cv2.VideoCapture(0)
baslangıc_vakti = 0
while True:
    bulundu = False
    merkez_x, merkez_y = 0, 0
    mesaj1, mesaj2 = "", ""
    bitis_zamani = time.time()
    ret, resim = kamera.read()
    resim_yukseklik, resim_genislik = resim.shape[:2]
    if not ret:
        break
    sonuclar = model(resim)
    for sonuc in sonuclar:
        for kutu in sonuc.boxes:
            x1, y1, x2, y2 = map(int, kutu.xyxy[0])
            nesne_id = int(kutu.cls[0])
            guven = kutu.conf[0]
            if nesne_id == 73:
                bulundu = True
                cv2.rectangle(resim, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(resim, f"Book: {guven:.2f}, Nesne ID: {nesne_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                merkez_x = (x1 + x2) // 2
                merkez_y = (y1 + y2) // 2
    #Gri çerçeve
    cv2.line(resim, (resim_genislik//2-50, resim_yukseklik//2-50), (resim_genislik//2+50, resim_yukseklik//2-50), (255, 255, 255), 1)
    cv2.line(resim, (resim_genislik//2-50, resim_yukseklik//2+50), (resim_genislik//2+50, resim_yukseklik//2+50), (255, 255, 255), 1)
    cv2.line(resim, (resim_genislik//2-50, resim_yukseklik//2-50), (resim_genislik//2-50, resim_yukseklik//2+50), (255, 255, 255), 1)
    cv2.line(resim, (resim_genislik//2+50, resim_yukseklik//2-50), (resim_genislik//2+50, resim_yukseklik//2+50), (255, 255, 255), 1)

    cv2.line(resim, (resim_genislik//2-20, resim_yukseklik//2), (resim_genislik//2+20, resim_yukseklik//2), (0, 0, 255), 2)
    cv2.circle(resim, (resim_genislik // 2, resim_yukseklik // 2), 4, (0, 0, 255), -1)
    cv2.line(resim, (resim_genislik//2, resim_yukseklik//2-20), (resim_genislik//2, resim_yukseklik//2+20), (0, 0, 255), 2)
    hata_x = merkez_x - (resim_genislik // 2)
    hata_y = merkez_y - (resim_yukseklik // 2)
    cv2.putText(resim, f"Hata X: {hata_x}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    cv2.putText(resim, f"Hata Y: {hata_y}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    fps = 1 / (bitis_zamani - baslangıc_vakti)
    cv2.putText(resim, f"FPS: {fps:.2f}", (490, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    if bulundu:
        if hata_x < -50:
            mesaj1 = f"CMD: ROTATE_LEFT {abs(hata_x)}"
            cv2.putText(resim, "Sola DONUYOR", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0, 0), 2)
        elif hata_x > 50:
            mesaj1 = f"CMD: ROTATE_RIGHT {hata_x}"
            cv2.putText(resim, "Saga DONUYOR", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0), 2)
        if hata_y < -50:
            mesaj2 = f"CMD: ROTATE_UP {abs(hata_y)}"
            cv2.putText(resim, "Yukari DONUYOR", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        elif hata_y > 50:
            mesaj2 = f"CMD: ROTATE_DOWN {hata_y}"
            cv2.putText(resim, "Asagi DONUYOR", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        if mesaj1 == "" and mesaj2 == "":
            cv2.putText(resim, "Nesne Merkezde Atese Hazir", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            mesaj1 = "CMD: HOVER"
        socet.sendto(mesaj1.encode() + " ".encode() + mesaj2.encode(), ("127.0.0.1", 5000))
    baslangıc_vakti = bitis_zamani
    cv2.imshow("Kamera", resim)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()