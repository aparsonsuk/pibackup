from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()
timestamp = datetime.now().strftime("%y%m%d_%H%M%S")

while True:
    pir.wait_for_motion()
    print("Motion detected")
    camera.start_recording("{}.h264".format(timestamp))
    pir.wait_for_no_motion()
    camera.stop_recording()
    sleep(1)
