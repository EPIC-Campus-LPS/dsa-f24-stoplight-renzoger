def button(yuh):
	while GPIO.input(18) == GPIO.LOW:  # function to take in a button press to turn on the stoplight pattern
		print ("GREEN")            # turning on the green LED and waiting 5 secs until its turned off
		GPIO.output(23,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(23,GPIO.LOW)
		print ("YELLOW")           # turning on the yellow LED (green+red LEDs) and waiting 1 sec until its turned off
		GPIO.output(21,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(21,GPIO.LOW)
		GPIO.output(23,GPIO.LOW)
		print ("RED")              # turning on the red LED and waiting 4 secs until its turned off
		GPIO.output(21,GPIO.HIGH)
		time.sleep(4)
		GPIO.output(21,GPIO.LOW)


import RPi.GPIO as GPIO                    # importing GPIO pins
import time                                # importing time
GPIO.setmode(GPIO.BCM)                     # setting up GPIO
GPIO.setwarnings(False)                    # ignoring warnings

GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # setting pin 18 as an input and setting its initial value as low (off)
GPIO.setup(25,GPIO.OUT)                            # setting pin 25 as an output
GPIO.setup(23,GPIO.OUT)                            # setting pin 23 as an output
GPIO.setup(21,GPIO.OUT)                            # setting pin 21 as an output
GPIO.add_event_detect(18,GPIO.RISING,callback=button) # setup event on pin 18
GPIO.output(23,GPIO.LOW) # keeping pin 23 on low (off) since it would stay on before button function is called

message = input("Press enter to quit\n\n") # an exit button if an error occurs or if done using the stoplight
