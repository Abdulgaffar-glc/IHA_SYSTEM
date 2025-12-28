import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))
while True:
    veriler, adres = sock.recvfrom(1024)
    print(f"Gelen veri: {veriler.decode()} - Gönderen adres: {adres}")