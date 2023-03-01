import RPi.GPIO as GPIO
import time

#핀 설정
priPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(priPin, GPIO.IN, GPIO.PUD_UP)

try:
	while(True):
		if GPIO.input(priPin) == GPIO.LOW:
			print("Detected")
		else:
			print("a")
		time.sleep(0.3)
except KeyboardInterrupt:
	GPIO.cleanup()
