import explorerhat
from time import sleep

def backwards(channel, event):
    explorerhat.motor.one.forward(50)
    explorerhat.motor.two.forward(50)
    sleep(1)
    explorerhat.motor.one.forward(0)
    explorerhat.motor.two.forward(0)
    sleep(0.5)
    
def forwards(channel, event):
    explorerhat.motor.one.backward(50)
    explorerhat.motor.two.backward(50)
    sleep(1)
    explorerhat.motor.one.backward(0)
    explorerhat.motor.two.backward(0)
    sleep(0.5)

def turn(channel, event):
    explorerhat.motor.one.forward(40)
    explorerhat.motor.two.backward(40)
    sleep(0.25)
    explorerhat.motor.one.forward(0)
    explorerhat.motor.two.backward(0)
    sleep(0.5)


while True:
    explorerhat.touch.one.pressed(forwards)
    explorerhat.touch.two.pressed(backwards)
    explorerhat.touch.three.pressed(turn)