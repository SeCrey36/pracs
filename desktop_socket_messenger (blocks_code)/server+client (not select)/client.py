import socket
import threading

def read_sok():
     while 1:
         data = sock.recv(1024)
         print(data.decode('utf-8'))
         
         
nickname = input('Your nick:') # Вводим наш псевдоним    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
print('Sock already')
sock.connect(('DESKTOP-0I1AUBD', 9090))  # подключемся к серверному сокету
print('Connected!')

potok = threading.Thread(target= read_sok)
potok.start() 

while 1:
     message = input()
     sock.send(('['+nickname+'] '+message).encode('utf-8'))