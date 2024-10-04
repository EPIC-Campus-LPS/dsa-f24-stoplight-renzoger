import RPi.GPIO as GPIO   # importing the GPIO pins
import time               # importing time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # setup
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
print ("GREEN")
GPIO.output(18,GPIO.HIGH) # setting GPIO 18 to high to turn on the LED
time.sleep(5)
GPIO.output(18,GPIO.LOW) # setting GPIO 18 to low to turn on the LED
print ("YELLOW")
GPIO.output(23,GPIO.HIGH) # setting GPIO 23 to high to turn on the LED
time.sleep(1)
GPIO.output(23,GPIO.LOW) # setting GPIO 23 to low to turn on the LED
print ("RED")
GPIO.output(21,GPIO.HIGH) # setting GPIO 21 to high to turn on the LED
time.sleep(4)
GPIO.output(21,GPIO.LOW) # setting GPIO 21 to low to turn on the LED

