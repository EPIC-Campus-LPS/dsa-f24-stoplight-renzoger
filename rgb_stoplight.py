import RPi.GPIO as GPIO    # importing the GPIO pins
import time                # importing time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)    # setup
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
print ("GREEN")            # setting GPIO 23 to high to turn on the LED
GPIO.output(23,GPIO.HIGH)
time.sleep(5)              # waiting 5 seconds
GPIO.output(23,GPIO.LOW)   # setting GPIO 23 to low to turn off the LED
print ("YELLOW")
GPIO.output(21,GPIO.HIGH)  # setting GPIO 21 to high to turn on the LED
GPIO.output(23,GPIO.HIGH)  # setting GPIO 23 to high to turn on the LED
time.sleep(1)              # waiting 1 second
GPIO.output(21,GPIO.LOW)   # setting GPIO 21 to low to turn off the LED
GPIO.output(23,GPIO.LOW)   # setting GPIO 23 to low to turn off the LED
print ("RED")
GPIO.output(21,GPIO.HIGH)  # setting GPIO 21 to high to turn on the LED
time.sleep(4)              # waiting 4 seconds
GPIO.output(21,GPIO.LOW)   # setting GPIO 21 to low to turn off the LED
