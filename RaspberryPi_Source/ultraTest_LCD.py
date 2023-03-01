from RPi_I2C_LCD_driver import RPi_I2C_driver
import RPi.GPIO as GPIO
import time

def measure():
	global start
	global stop
	GPIO.output(triggerPin, True)
	time.sleep(0.00001) #10us
	GPIO.output(triggerPin, False)
	while GPIO.input(echoPin) == False:
		start = time.time() # echo High
	while GPIO.input(echoPin) == True:
		stop = time.time() #echo Low
	print("stop : ", stop)
	print("start : ", start)
	elapsed = stop - start
	print(elapsed)
	distance = (elapsed * 34000) / 2 # cm/us
	return distance

start = 0
stop = 0
triggerPin = 13 #trigger
echoPin = 6 # echo
warningPin = 23 #경고핀

#lcd set
lcd = RPi_I2C_driver.lcd(0x27)
lcd.clear()
lcd.setCursor(0, 0)
lcd.print("Distance")

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(warningPin, GPIO.OUT)
s = GPIO.PWM(warningPin, 1000)
try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" %distance)
		lcd.setCursor(0,1)
		inputStr = "%.2f cm" % distance
		
		lcd.print("%16s cm" % inputStr)
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
			time.sleep(0.5)
except KeyboardInterrupt:
	lcd.clear()
	GPIO.cleanup()
