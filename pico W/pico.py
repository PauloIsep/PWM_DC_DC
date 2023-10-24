from machine import Pin, ADC, PWM          # Do modulo machine importa as classes pin ADC e PWM
import ujson
import os
import network
import socket
import machine
from time import sleep                     # Do modulo time importa a class sleep 
led=PWM(Pin(0))             #Define Pin GPIO 13 como Output do PWM gerado

led = machine.Pin(0, machine.Pin.OUT)

#fre=ADC(27)   #Define o GPIO 27 com entrada
#ciclo=ADC(28)        #creating potentiometer object

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NOS-DCEF', '7XXAUKKP')

max_wait = 10
print('Waiting for connection')
while max_wait > 10:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1    
    sleep(1)
status = None
if wlan.status() != 3:
    raise RuntimeError('Connections failed')
else:
    status = wlan.ifconfig()
    print('connection to', 'NOS','succesfull established!', sep=' ')
    print('IP-adress: ' + status[0])
ipAddress = status[0]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5000))
s.listen(1)
print('Waiting for a connection...')

while True:
    conn, addr = s.accept()
    print('Connection from', addr)

    # Receive a command from the client
    data = conn.recv(1024).decode() #1024 
    print(data)
    command = ujson.loads(data)
    print(command)

    # Turn the GPIO pin on or off based on the received command
    if command['frequencia'] == '50':
        print('Turning LED on...')
        led.value(1)
    elif command['duty_cycle'] == '60':
        print('Turning LED off...')
        led.value(0)
    else:
        print('Error')
    conn.close()




'''

while True:
  
  freq= (fre.read_u16()//10)+3447#ler pin   
  print ('Valor Frequencia' ,freq) 
  if freq <2000 :
      led.freq(2000)
  elif freq > 8000:
      led.freq(8000)
  else:     
      led.freq(freq)   
  r_ciclica=ciclo.read_u16()           #le ADC
  print('Valor duty', r_ciclica)
  
  
  if  r_ciclica < 500 :
      led.duty_u16(0)
  elif r_ciclica > 49151:
      led.duty_u16(49151)
  else:     
      led.duty_u16(r_ciclica) 
  sleep(0.25)

  '''