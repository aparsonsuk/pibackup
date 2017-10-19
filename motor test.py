import explorerhat

def forward (channel,event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
def backward (channel,event):
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
def right (channel,event):
    explorerhat.motor.one.backward(35)
    explorerhat.motor.two.forward(35)   
def left (channel,event):
    explorerhat.motor.one.forward(35)
    explorerhat.motor.two.backward(35)
def stop (channel, event):
    explorerhat.motor.one.forward(0)
    explorerhat.motor.two.forward(0)


explorerhat.touch.one.pressed(forward)
explorerhat.touch.two.pressed(backward)
explorerhat.touch.three.pressed(right)
explorerhat.touch.four.pressed(stop)