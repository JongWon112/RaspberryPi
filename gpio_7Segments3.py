import RPi.GPIO as GPIO
import time
import threading

A = 2
B = 3
C = 4
D = 17
E = 27
F = 22
G = 10
D1 = 25
D2 = 8
D3 = 7
D4 = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)

numList = [
	[1,1,1,1,1,1,0], #0
	[0,1,1,0,0,0,0], #1
	[1,1,0,1,1,0,1], #2
	[1,1,1,1,0,0,1], #3
	[0,1,1,0,0,1,1], #4
	[1,0,1,1,0,1,1], #5
	[1,0,1,1,1,1,1], #6
	[1,1,1,0,0,1,0], #7
	[1,1,1,1,1,1,1], #8
	[1,1,1,0,0,1,1]  #9
]
pinList = [A, B, C, D, E, F, G]
outputList = [D1, D2, D3, D4]
startNumber = 1


try:
	while startNumber <= 10000:
		#초기화
		for i in range(4):
			for j in range(7):
				GPIO.output(pinList[j], False)
			GPIO.output(outputList[i], True)
		#숫자 세팅
		showList = list(str(startNumber).zfill(4))  # 문자열 형태로 각 자리수에 입력할 숫자
		loopTime = 0
		while(loopTime <= 0.1):
			for i in range(4):
				GPIO.output(outputList[i], False)
				for j in range(7):
					GPIO.output(pinList[j],numList[int(showList[i])][j])
				time.sleep(0.0005)
				loopTime += 0.0005
				for j in range(7):
					GPIO.output(pinList[j], False)
				GPIO.output(outputList[i], True)
		startNumber += 1
except KeyboardInterrupt:
	GPIO.cleanup()
