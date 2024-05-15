import socket

print('For exit from server: `exit`, `quit` or `q`.')

HOST = '127.0.0.1'
PORT = 8080


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Already connected!')
    while True:
        
        mess = input('\nInput your message >>> ')
        if any(mess.lower() in ext for ext in ['quit', 'exit', 'q']):
            break
        mess = mess.encode('utf-8')
        s.sendall(mess)
        data = s.recv(1024)
        print('\nRecieved: ', data.decode('utf-8'))