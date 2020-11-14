import socket
import network
from machine import Pin
from time import sleep

omg = network.WLAN(network.STA_IF)
omg.active(False)
wlan = network.WLAN(network.AP_IF)
wlan.active(True)
wlan.config(essid = 'ilovecocks', password = '12345678')
#wlan.connect('Putin', 'zaPutina01101')
#wlan.connect('Robo', '22222222')

sleep(5)
wlan.ifconfig()
#wlan.isconnected()

HOST = ''
PORT = 5007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
a = Pin(5, Pin.OUT) #   D1    Добавление выводов на L293
b = Pin(4, Pin.OUT) #   D2
c = Pin(14, Pin.OUT) #   D5
d = Pin(12, Pin.OUT) #   D6

#wlan.isconnected()

conn, addr = s.accept()
print ('Connected by', addr)

while True:
  data = conn.recv(1)
  print(data)
  if data == b'3': #Назад - оба движка идут назад
    d.value(0)
    b.value(0)
    a.value(1)
    c.value(1)
  elif data == b'1': #Вперед
    a.value(0)
    c.value(0)
    b.value(1)
    d.value(1)
  elif data == b'2': #Вправо (2Правый назад, левый вперед)
    b.value(0)
    c.value(0)
    a.value(1)
    d.value(1)
  elif data == b'4': #Влево (Левый назад, правый впередСейчас обх)
    a.value(0)
    d.value(0)
    b.value(1)
    c.value(1)
  else:
    a.value(0) #Выключил
    b.value(0)
    c.value(0)
    d.value(0)