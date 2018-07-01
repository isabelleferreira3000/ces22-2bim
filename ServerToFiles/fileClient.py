# Não Lista os arquivos que já estão no servidor, nem fazia upload
# Teoricamente fazia download de arquivos que estão no servidor, mas
# está dando algum erro que eu não soube ajeitar

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = input("Filename? -> ")
    filename = bytes(filename.encode('ascii'))
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = int(data[6:])
            message = input("File Exists, " + str(filename) + "Bytes, download (Y/N)? -> ")
            if message == 'Y':
                s.send = 'OK'
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print("{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done")
                print("Download Complete!")
        else:
            print("File does not Exist!")
    s.close()


if __name__ == '__main__':
    Main()