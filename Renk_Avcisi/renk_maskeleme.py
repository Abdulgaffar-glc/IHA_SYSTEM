import cv2
import numpy as np
kamera = cv2.VideoCapture(0)
while True:
    ret, resim = kamera.read()
    if not ret:
        break

    hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    alt_sinir = np.array([100,150,50])
    ust_sinir = np.array([140,255, 255])
    maske = cv2.inRange(hsv_resim, alt_sinir, ust_sinir)
    sonuc = cv2.bitwise_and(resim, resim, mask=maske)
    cv2.imshow("Orijinal", resim)
    cv2.imshow("Maske", maske)
    cv2.imshow("Sonuc", sonuc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()