import socket
import ssl
import threading
from U_GlobalVariables import IPv4IDofServer, portNumberOfServer,dosyaAdi

def istemci_ile_ilgilen(stream, dosya):
    print('-----------------------------------------\n')
    while True:
        veri = stream.recv(1024)
        if not veri:
            break
        else:
            dosya.write(veri)

    print('Dosya alındı, bağlantı kapatılıyor...')
    print('-----------------------------------------\n')
    dosya.close()

index = 1

baglam = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
baglam.load_cert_chain(certfile="serverCertificate/server.crt", keyfile="serverCertificate/serverPriv.key")
baglam.options |= ssl.OP_NO_SSLv2
baglam.options |= ssl.OP_NO_SSLv3

bSoket = socket.socket()
bSoket.bind(('192.168.1.48', 555))
bSoket.listen(5)

while True:
    yeniSoket, fromaddr = bSoket.accept()
    akis = baglam.wrap_socket(yeniSoket, server_side=True)
    dosya = open('şifrelenmiş#' + str(index), 'wb')
    index += 1

    print("'Bağlantı kuruldu: " + str(fromaddr))
    try:
        p1 = threading.Thread(target=istemci_ile_ilgilen, args=(akis, dosya))
        p1.start()
    except KeyboardInterrupt:
        break
    except Exception:
        print('\n İstemci işleme hatası\n')
        break

print('\n-----------------------------------------')
print('Sunucu kapatılıyor...\n')
