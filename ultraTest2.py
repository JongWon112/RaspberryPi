import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(triggerPin, True)
	time.sleep(0.00001) #10us
	GPIO.output(triggerPin, False)

	while GPIO.input(echoPin) == False:
		start = time.time() # echo High
	while GPIO.input(echoPin) == True:
		stop = time.time() #echo Low
	elapsed = stop - start
	distance = (elapsed * 34000) / 2 # cm/us
	return distance

triggerPin = 2 #trigger
echoPin = 3 # echo
warningPin = 4 #경고핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(warningPin, GPIO.OUT)
s = GPIO.PWM(warningPin, 1000)
try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" %distance)
		if distance < 5:
			s.start(50)
			
		elif distance < 100:
			s.stop()
			s.start(50)
			sTime = distance * 0.1/10
			time.sleep(0.1)
			s.stop()
			time.sleep(sTime)
		else:
			s.stop()
except KeyboardInterrupt:
	GPIO.cleanup()
