import socket
import ssl
from U_GlobalVariables import IPv4IDofServer, portNumberOfServer,dosyaAdi

def dosya_gonder():
    sunucu_adresi = '192.168.1.48'
    port_numarasi = 555
    dosya_adi = dosyaAdi
    dosya_adi2 = "b.jpg"
    print(dosya_adi)
    print(dosya_adi2)

    bayrak = 1

    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglam = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

        baglam.verify_mode = ssl.CERT_REQUIRED
        baglam.check_hostname = False
        baglam.load_verify_locations("CACertificate/CArsa.crt")

        baglam.options |= ssl.OP_NO_SSLv2
        baglam.options |= ssl.OP_NO_SSLv3

        ssl_baglantisi = baglam.wrap_socket(soket, server_hostname=sunucu_adresi)
        ssl_baglantisi.connect((sunucu_adresi, port_numarasi))

    except Exception as hata:
        print(hata)
        bayrak = 0

    if bayrak == 1:
        try:
            # Gönderilecek dosyayı aç
            gonderilecek_dosya = open(dosya_adi, 'rb')

            # Döngüye başlamadan önce 'veri'yi başlat
            veri = gonderilecek_dosya.read(1024)

            while veri:
                ssl_baglantisi.send(veri)
                veri = gonderilecek_dosya.read(1024)
        except Exception as hata:
            print(hata)
        finally:
            gonderilecek_dosya.close()
            ssl_baglantisi.close()
            print('Dosya ' + dosya_adi + ' gönderme tamamlandı')

# Directly call the file transfer function
dosya_gonder()
