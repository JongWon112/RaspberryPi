import RPi.GPIO as GPIO
import time
import getch

pinA = 2
pinB = 3
pinC = 4
pinD = 17
pinE = 27
pinF = 22
pinG = 10

GPIO.setmode(GPIO.BCM)

GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)
GPIO.setup(pinC, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)
GPIO.setup(pinE, GPIO.OUT)
GPIO.setup(pinF, GPIO.OUT)
GPIO.setup(pinG, GPIO.OUT)

pinList = [pinA, pinB, pinC, pinD, pinE, pinF, pinG]

numList = [
	[0,0,0,0,0,0,1], #0
	[1,0,0,1,1,1,1], #1
	[0,0,1,0,0,1,0], #2
	[0,0,0,0,1,1,0], #3
	[1,0,0,1,1,0,0], #4
	[0,1,0,0,1,0,0], #5
	[0,1,0,0,0,0,0], #6
	[0,0,0,1,1,0,1], #7
	[0,0,0,0,0,0,0], #8
	[0,0,0,1,1,0,0] # 9
]


try:
	while True:
		ch = int(getch.getch())
		for i in range(7):
			GPIO.output(pinList[i], numList[ch][i])
except KeyboardInterrupt:
	GPIO.cleanup()
