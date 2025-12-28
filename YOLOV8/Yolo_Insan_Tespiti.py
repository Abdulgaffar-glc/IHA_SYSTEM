from ultralytics import YOLO
import cv2
import time
model = YOLO("yolov8n.pt")
model.to("cpu")
baslangic_zamani = 0
camera = cv2.VideoCapture(0)
while True:
    bitis_zamani = time.time()
    kontrol, resim = camera.read()
    if not kontrol:
        break
    sonuclar = model(resim)
    for sonuc in sonuclar:
        boxes = sonuc.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            nesne_id = int(box.cls[0])
            guven_skori = box.conf[0]
            if nesne_id == 0 and guven_skori > 0.5:
                cv2.rectangle(resim, (x1, y1), (x2, y2), (0, 0, 255), 2)
                dikdortgen_merkez = ((x1 + x2) // 2, (y1 + y2) // 2)
                cv2.circle(resim, dikdortgen_merkez, 5, (0, 255, 255), -1)
                cv2.putText(resim, f'Insan: {guven_skori:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    fps = 1 / (bitis_zamani - baslangic_zamani)
    baslangic_zamani = bitis_zamani
    genislik, yukseklik = resim.shape[:2]
    if fps < 30:
        cv2.putText(resim, f"FPS: {int(fps)}", (520, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(resim, f"FPS: {int(fps)}", (520, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Yolo Insan Tespiti", resim)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()