import RPi.GPIO as GPIO
import time
import threading

A, B, C, D, E, F, G = 2, 3, 4, 17, 27, 22, 10
D1, D2, D3, D4 = 25, 8, 7, 1
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

#각 숫자별 pin 입력값
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
#출력 대상 리스트
outputList = [D1, D2, D3, D4]
placeList = []
threadFlag = False

#GPIO.output(D1, True)
#GPIO.output(D2, True)
#GPIO.output(D3, True)
#GPIO.output(D4, True)

#GPIO.output(A, False)
#GPIO.output(B, False)
#GPIO.output(C, False)
#GPIO.output(D, False)
#GPIO.output(E, False)
#GPIO.output(F, False)
#GPIO.output(G, False)

def showNumber():
	global threadFlag
	while threadFlag == True:
		for i in range(4):
			GPIO.output(outputList[i], False)
			for j in range(7):
				GPIO.output(pinList[j], numList[placeList[i]][j])
			time.sleep(0.0005)
			for j in range(7):
				GPIO.output(pinList[j], False)
			GPIO.output(outputList[i],True)
	#스레드 종료 시 세팅 초기화
	for i in range(4):
		for j in range(7):
			GPIO.output(pinList[j], False)
		GPIO.output(outputList[i], True)
	return

try:
	while True:
		thread = threading.Thread(target = showNumber)
		number = int(input())
		threadFlag = False # 진행중인 스레드 종료플레그
		time.sleep(0.005) #진행중인 스레드 종료까지 대기시간..
		placeList = list(map(int,str(number))) #입력값 리스트로 담는다.
		threadFlag = True #새로운 스레드 실행플레그
		thread.start()
except KeyboardInterrupt:
	GPIO.cleanup()
