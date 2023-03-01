import RPi.GPIO as GPIO
import time

led = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

m = GPIO.PWM(led, 1000)
m.start(0) # 1000Hz

try:
	while True:
		for dc in range(0, 101, 1): #duty 0~100
			m.ChangeDutyCycle(dc)
			time.sleep(0.05)

		for dc in range(100, 0, -1):
			m.ChangeDutyCycle(dc)
			time.sleep(0.05)
except KeyboardInterrupt:
	m.stop()
	GPIO.cleanup()
