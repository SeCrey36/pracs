import select, socket

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(5)
sock.setblocking(False)
inputs = [sock]  # сокеты для чтения
outputs = []     # сокеты для записи
messages ={}     # сообщения для сокетов
clients = []     # список всех сокетов в онлайне

print('Server already!')

            
while True:
    #print(clients)
    #print('')
    # вызов 'select' который проверяет сокеты и по готовности вернет 3 списка
    reads, send, excepts = select.select(inputs, outputs, inputs)

    # Сокеты готовые к чтению
    for conn in reads:
        if conn == sock:
            new_conn, client_addr = conn.accept() # Новый клиент, принимаем подключение
            print('Connected!')
            new_conn.setblocking(False) # устанавливаем неблокирующий сокет
            inputs.append(new_conn) # поместим новый сокет на прослушку
            clients.append(new_conn) # добавим сокет в общий список
            
        else:
            try:
                data = conn.recv(1024) # если это НЕ серверный сокет то слушаем
                #print(data)
            except:
                print('Error while recieve')
                
            if data:
                # Кладем сообщение в словарь, {сокет:сообщение}
                if messages.get(conn, None):
                    messages[conn].append(data)
                else:
                    messages[conn] = [data]

                # добавляем соединение клиента в очередь 
                # на готовность к приему сообщений от сервера
                if conn not in outputs:
                    outputs.append(conn)
            else:
                print('Client disconnected')
                # если сообщений нет, то клиент отвалился
                # удаляем его из всех очередей
                if conn in outputs:
                    outputs.remove(conn)
                inputs.remove(conn)
                clients.remove(conn)
                # закрываем сокет
                conn.close()
                # удаляем сообщения для данного сокета
                if messages.get(conn, None):
                    del messages[conn]

    # Сокеты готовые принять сообщение
    for conn in send:
        # выбираем из словаря сообщения
        # для данного сокета
        # for message in messages:
        #     # temp = message.pop(0).decode('utf-8').upper()
        #     # conn.send(temp.encode())
        
        msg = messages.get(conn, None)
        print(msg)
        if len(msg):
            # если есть сообщения - то переводим 
            # его в верхний регистр и отсылаем
            temp = msg.pop(0).decode('utf-8').upper()
            print(temp)
            conn.send(temp.encode())
        else:
            # если нет сообщений - удаляем из очереди
            # сокетов, готовых принять сообщение
            outputs.remove(conn)

    # Сокеты в которых произошла ошибка
    for conn in excepts:
        print('Error client')
        # удаляем сокет с ошибкой из всех очередей
        inputs.remove(conn)
        clients.remove(conn)
        if conn in outputs:
            outputs.remove(conn)
        conn.close() # Закрытие сокета клиента с ошибкой
        # удаляем сообщения для данного сокета
        del messages[conn]