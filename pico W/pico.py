from machine import Pin, ADC, PWM          # Do modulo machine importa as classes pin ADC e PWM
import json
from time import sleep                     # Do modulo time importa a class sleep 
led=PWM(Pin(13))             #Define Pin GPIO 13 como Output do PWM gerado


#fre=ADC(27)   #Define o GPIO 27 com entrada
#ciclo=ADC(28)        #creating potentiometer object

file = open ('parameters.json','r' )
data = json.load(file)


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