from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
model.to("cpu") 
camera = cv2.VideoCapture(0)
while True:
    kontrol, resim = camera.read()
    if not kontrol:
        break
    sonuc = model(resim)
    cizilmis_resim = sonuc[0].plot()
    cv2.imshow("Yolo Nesne Tespiti", cizilmis_resim)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()