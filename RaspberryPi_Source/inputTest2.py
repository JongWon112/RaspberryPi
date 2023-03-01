import RPi.GPIO as GPIO
import time

switchPin = 7
ledPin = 3
offPin =36

GPIO.setmode(GPIO.BCM)

GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(offPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

switchFlag = False

try:
	while True:
		if GPIO.input(switchPin) == False:
			time.sleep(0.3)
			if switchFlag == False:
				print("lamp On")
				switchFlag = True
				GPIO.output(ledPin, GPIO.HIGH)
			else:
				print("lamp Off")
				switchFlag = False
				GPIO.output(ledPin, GPIO.LOW)
		if GPIO.input(offPin) == False:
			if switchFlag == True:
				time.sleep(0.3)
				print("lamp Off")
				switchFlag = False
				GPIO.output(ledPin, GPIO.LOW)
except KeyboardInterrupt:
	GPIO.cleanup()
