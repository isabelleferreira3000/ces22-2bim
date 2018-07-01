import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
ip = str(socket.gethostbyname(socket.gethostname()))
port = 1236

clients = {}

s.bind((ip, port))
s.listen()
print('Server Ready...')
print('Ip Address of the Server::%s' % ip)


def handle_client(client, user_name):
    clientConnected = True
    keys = clients.keys()
    help = 'There are four commands in Messenger\n'
    help = help + '1::**chatlist=>gives you the list of the people currently online\n'
    help = help + '2::**quit=>To end your session\n'
    help = help + '3::**broadcast=>To broadcast you message to each and every person currently present online\n'
    help = help + '4::Add the name of the person  at the end of your message preceded by ** ' \
                  'to sent it to a particular person\n'

    while clientConnected:
        msg = client.recv(1024).decode('ascii')
        response = 'Number of People Online\n'
        found = False
        if '**chatlist' in msg:
            clientNo = 0
            for name in keys:
                clientNo += 1
                response = response + str(clientNo) + '::' + name + '\n'
            client.send(response.encode('ascii'))
        elif '**help' in msg:
            client.send(help.encode('ascii'))
        elif '**broadcast' in msg:
            msg = msg.replace('**broadcast', '')
            for k,v in clients.items():
                v.send(msg.encode('ascii'))
        elif '**quit' in msg:
            response = 'Stopping Session and exiting...'
            client.send(response.encode('ascii'))
            clients.pop(user_name)
            print(user_name + ' has been logged out')
            clientConnected = False
        else:
            for name in keys:
                if ('**' + name) in msg:
                    msg = msg.replace('**' + name, '')
                    clients.get(name).send(msg.encode('ascii'))
                    found = True
            if not found:
                client.send('Trying to send message to invalid person.'.encode('ascii'))


while serverRunning:
    client, address = s.accept()
    user_name = client.recv(1024).decode('ascii')
    print('%s connected to the server' % str(user_name))
    client.send('Welcome to Messenger'.encode('ascii'))

    if client not in clients:
        clients[user_name] = client
        threading.Thread(target=handle_client, args=(client, user_name, )).start()
