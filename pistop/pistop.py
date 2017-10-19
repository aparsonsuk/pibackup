from time import sleep
from gpiozero import LED
 
r = LED(22)
a = LED(27)
g = LED(17)

while True:
    r.on()
    sleep(5)
    r.off()
    sleep(5)
