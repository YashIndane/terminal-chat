import socket
import threading
import os
import datetime

print('')

family = socket.AF_INET
protocol = socket.SOCK_DGRAM

socket1 = socket.socket(family , protocol)
server_ip1 = input('enter your ip : ')
server_port1 = int(input('enter your port number : '))
socket1.bind((server_ip1 , server_port1))

socket2 = socket.socket(family , protocol)
server_ip2 = input('enter other end ip : ')
server_port2 = int(input('enter other end port number : '))

print('')

def time():

   t = str(datetime.datetime.now())
   t = t.split(' ')[1][:5]
   return t

def receive():
  while 1:
    
    buffer_size = 1024
    msg = socket1.recvfrom(buffer_sizeo)
    os.system('tput setaf 32')
    print('\U0001F464' + ' ' + msg[0].decode())
    os.system('tput setaf 7')
    t_ = time()
    print('__'*(36) + t_ + '\n')

def send():
  while 1:

    msg = input()
    socket2.sendto(msg.encode() , (server_ip2 , server_port2))
    t_ = time()
    print('__'*(36) + t_ + '\n')

print('~'*(32) + 'TERMINAL-CHAT' + '~'*(32) + '\n')

receiveThread = threading.Thread(target = receive)
sendThread = threading.Thread(target = send)

receiveThread.start()
sendThread.start()




