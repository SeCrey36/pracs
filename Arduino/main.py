import machine
n1 = machine.Pin(0,machine.Pin.OUT) #5
n2 = machine.Pin(2,machine.Pin.OUT) #0
n3 = machine.Pin(4,machine.Pin.OUT) #4
n4 = machine.Pin(5,machine.Pin.OUT) #2

import network

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    sta.connect('test1', 'nodemcutest')
    while not sta.isconnected():
        pass
print('network config:', sta.ifconfig())

# ************************

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80)) 
s.listen(5)



while True:
    conn, addr = s.accept()
    request=conn.recv(1024)

    request = str(request)
    forward_on = request.find('/?forward=1')
    forward_off = request.find('/?forward=0')
    
    back_on = request.find('/?back=1')
    back_off = request.find('/?back=0')
    
    left_on = request.find('/?left=1')
    left_off = request.find('/?left=0')
    
    right_on = request.find('/?right=1')
    right_off = request.find('/?right=0')
    
    if forward_on == 6:
        n1.value(1)
        n3.value(1)
    elif forward_off == 6:
        n1.value(0)
        n2.value(0)
        n3.value(0)
        n4.value(0)
    elif back_on == 6:
        n2.value(1)
        n4.value(1)
    elif left_on == 6:
        n2.value(1)
        n3.value(1)
    elif right_on == 6:
        n1.value(1)
        n4.value(1)

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/plain\n')
    conn.send('Connection: close\n\n')

    conn.close()