from picamera import PiCamera
from time import sleep 
from gpiozero import Button

button = Button(17)
camera = Picamera()

camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/doorbell.jpg')
camera.stop_preview()