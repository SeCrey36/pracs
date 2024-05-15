import socket, threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind (('0.0.0.0', 8080))
sock.listen(10)  # Кол-во соединений
clients = [] # Клиенты
end = []
print ('Server already')


def accept():
    while True:
        client, addr = sock.accept()
        clients.append(client)
        print(f'Клиент подключился! Адрес: {addr}. Количество подключений: {len (clients)}')


def recv_data(client): # Принятие информации от клиентов
    while True:
        try:
            indata = client.recv(1024)
        except:
            clients.remove(client)
            end.remove(client)
            print(f'Клиент отключился! Количество подключений: {len (clients)}')
            break
        print(indata.decode('utf-8'))
        for clien in clients: # Отправить всем полученное
            if clien != client:
                clien.send(indata)

def indatas():
    while True:
                 # Выполните цикл подключенных клиентов и создайте соответствующий поток
            for clien in clients:
                                 # Если поток уже существует, пропустить
                if clien in end:
                    continue
                index = threading.Thread(target = recv_data,args = (clien,))
                index.start()
                end.append(clien)

def outdatas():
    while True:
                 # Введите информацию, которая будет предоставлена ​​клиенту
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            break
            print ('Отправить всем:% s'% outdata)
                 # Отправлять информацию каждому клиенту
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))

# Создать многопоточность
 # Создать получающую информацию, объект потока
t1 = threading.Thread(target = indatas,name = 'input')
t1.start()
 
 # Создать отправляемое сообщение, объект потока
t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()
 
 # Ожидание подключения клиента, объект потока
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()
 
 # Блокировать округ, пока подпоток не будет завершен, и основной поток не может закончиться
# t1.join()
t2.join()
 
 # Выключите все серверы
for client in clients:
    client.close()

print ('-' * 5 + 'сервер отключен' + '-' * 5)