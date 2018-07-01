import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1236

user_name = input('Enter user name::')

ip = input('Enter the IP Address::')

s.connect((ip, port))
s.send(user_name.encode('ascii'))

clientRunning = True


def receive_msg(sock):
    while clientRunning:
        msg = sock.recv(1024).decode('ascii')
        print(msg)


threading.Thread(target=receive_msg, args=(s,)).start()

while clientRunning:
    tempMsg = input()
    msg = user_name + '>>' + tempMsg
    if '**quit' in msg:
        clientRunning = False
        s.send('**quit'.encode('ascii'))
    else:
        s.send(msg.encode('ascii'))
