# İHA Görüntü İşleme ile Nesne Takibi

Bu proje, kamera görüntüsü üzerinden **YOLOv8** kullanarak nesne tespiti yapan ve tespit edilen nesnenin ekran merkezine göre konumunu hesaplayıp basit yönlendirme komutları üreten bir **İHA simülasyon prototipidir**.

---

## Özellikler

* Gerçek zamanlı kamera görüntüsü
* YOLOv8 ile nesne tespiti
* Nesne merkez noktası hesaplama
* Ekran merkezine göre X–Y hata hesabı
* Görsel nişangâh (crosshair)
* FPS gösterimi
* UDP üzerinden komut gönderimi

---

## Kullanılan Teknolojiler

* Python
* OpenCV
* Ultralytics YOLOv8
* UDP Socket


* Çıkış için **q** tuşuna bas.
* Komutlar `127.0.0.1:5000` adresine UDP ile gönderilir.

---

## Notlar

* YOLOv8n (COCO) modeli kullanılmıştır.
* Test amacıyla `ID = 73 (book)` sınıfı takip edilmektedir.
* Simülasyon ve öğrenme amaçlı hazırlanmıştır.

---

## Geliştirici

**Abdulgaffar Gülice**

