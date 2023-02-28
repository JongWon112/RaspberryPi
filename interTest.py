import RPi.GPIO as GPIO
import time

interPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(interPin, GPIO.IN, GPIO.PUD_UP) #내부 pull_pu 사요

def ledBlink(channel):
	print("INTERRUPT")

GPIO.add_event_detect(interPin, GPIO.RISING, callback=ledBlink,
					 bouncetime=300)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
