from machine import *
from time import *
ir=Pin(5,Pin.IN)
while True:
  a=ir.value()
  print(a)
  sleep(0.5)

