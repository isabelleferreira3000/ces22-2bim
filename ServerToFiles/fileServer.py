# Não Lista os arquivos que já estão no servidor, nem fazia upload
# Teoricamente fazia download de arquivos que estão no servidor, mas
# está dando algum erro que eu não soube ajeitar

import socket
import threading
import os


def RetrFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        bla = "EXISTS " + str(os.path.getsize(filename))
        bla = bytes(bla.encode('ascii'))
        sock.send(bla)
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != '':
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR")

    sock.close()


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print("Server Started.")
    while True:
        c, addr = s.accept()
        print("client connected ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("retrThread", c))
        t.start()


if __name__ == '__main__':
    Main()
