from machine import Pin
import time

l1 = Pin(14, Pin.OUT)
l2 = Pin(25, Pin.OUT)
l3 = Pin(26, Pin.OUT)
l4 = Pin(27, Pin.OUT)

list2 = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

while True:
    for i in list2:
        l1.value(i[0])
        l2.value(i[1])
        l3.value(i[2])
        l4.value(i[3])
        time.sleep(0.005)
