import socket
import threading
import os
import datetime


sc = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
server_ip = ''
server_port = 
sc.bind((server_ip , server_port))

sc1 = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
sip = ''
spo = 

def time():

   t = str(datetime.datetime.now())
   t = t.split(' ')[1][:5]
   return t

def rc():
  while 1:

    msg = sc.recvfrom(512)
    os.system('tput setaf 3')
    print(msg[0].decode())
    os.system('tput setaf 7')
    t_ = time()
    print('__'*(36) + t_ + '\n')

    

def se():
  while 1:

    msg = input()
    sc1.sendto(msg.encode() , (sip , spo))
    t_ = time()
    print('__'*(36) + t_ + '\n')

x1 = threading.Thread(target=rc)
x2 = threading.Thread(target=se)
x1.start()
x2.start()



