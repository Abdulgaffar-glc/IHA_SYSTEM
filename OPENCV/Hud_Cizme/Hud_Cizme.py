import cv2
camera =cv2.VideoCapture(0)
while True:
    kontrol, resim =  camera.read()
    if not kontrol:
        break
    yukseklik, genislik, kanal = resim.shape
    cv2.putText(resim,"SISTEM AKTIF",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
    cv2.circle(resim,(genislik//2,yukseklik//2),30,(0,0,255),3)
    cv2.circle(resim,(genislik//2,yukseklik//2),5,(255,0,255),3)
    cv2.imshow("Goruntu",resim)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
