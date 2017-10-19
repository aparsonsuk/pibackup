from time import sleep
from gpiozero import LED
 
r = LED(22)
a = LED(27)
g = LED(17)

for i in range(5):
    r.on()
    sleep(5)
    a.on()
    sleep(1.5)
    r.off()
    a.off()
    g.on()
    sleep(5)
    g.off()
    a.on()
    sleep(1.5)
    a.off()
