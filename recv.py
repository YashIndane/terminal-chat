import socket
import threading
import os
import datetime

print('')
sc = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
server_ip = input('enter your ip : ')
server_port = int(input('enter your port number : '))
sc.bind((server_ip , server_port))

sc1 = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
sip = input('enter other end ip : ')
spo = int(input('enter other end port number : '))
print('')

def time():

   t = str(datetime.datetime.now())
   t = t.split(' ')[1][:5]
   return t

def receive():
  while 1:

    msg = sc.recvfrom(1024)
    os.system('tput setaf 32')
    print('\U0001F464' + ' ' + msg[0].decode())
    os.system('tput setaf 7')
    t_ = time()
    print('__'*(36) + t_ + '\n')

def send():
  while 1:

    msg = input()
    sc1.sendto(msg.encode() , (sip , spo))
    t_ = time()
    print('__'*(36) + t_ + '\n')

print('~'*(32) + 'TERMINAL-CHAT' + '~'*(32) + '\n')

receiveThread = threading.Thread(target = receive)
sendThread = threading.Thread(target = send)

receiveThread.start()
sendThread.start()




