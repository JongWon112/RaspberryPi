# RaspberryPi 

1. RaspberryPi 4-Digit FND
  - 입출력 핀 세팅
<pre>
<code>
import RPi.GPIO as GPIO
import time
import threading

#pin 지정
A, B, C, D, E, F, G = 2, 3, 4, 17, 27, 22, 10
D1, D2, D3, D4 = 25, 8, 7, 1
#BCM mode로 설정
GPIO.setmode(GPIO.BCM)

pinList = [A, B, C, D, E, F, G] #숫자를  표시할  핀리스트
outPinList = [D1, D2, D3, D4]   #표시할 위치 리스트

#pin 초기화
for pin in pinList:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

for outPin in outPinList:
	GPIO.setup(outPin, GPIO.OUT)
	GPIO.output(outPin, GPIO.HIGH)

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

#출력할 숫자 4개
outNum = []
#쓰레드 플레그
threadFlag = False

</code>
</pre>
  - outNum 숫자를 표시하는 thread
<pre>
<code>

def showNumber():
	global threadFlag
	while threadFlag == True:
		for i in range(4):
			GPIO.output(outPinList[i], False)
			for j in range(7):
				GPIO.output(pinList[j], numList[outNum[i]][j])
			time.sleep(0.0005)
			for j in range(7):
				GPIO.output(pinList[j], False)
			GPIO.output(outPinList[i],True)
	#스레드 종료 시 세팅 초기화
	for i in range(4):
		for j in range(7):
			GPIO.output(pinList[j], False)
		GPIO.output(outPinList[i], True)
	return

try:
	while True:
		thread = threading.Thread(target = showNumber)
		number = int(input())
		threadFlag = False # 진행중인 스레드 종료플레그
		time.sleep(0.005) #진행중인 스레드 종료까지 대기시간..
		outNum = list(map(int,str(number))) #입력값 리스트로 담는다.
		threadFlag = True #새로운 스레드 실행플레그
		thread.start()
except KeyboardInterrupt:
	GPIO.cleanup()
</code>
</pre>
 
  - 입력받기 , thread 실행
<pre>
<code>
try:
	while True:
		thread = threading.Thread(target = showNumber)
		number = int(input())
		threadFlag = False # 진행중인 스레드 종료플레그
		time.sleep(0.005) #진행중인 스레드 종료까지 대기시간..
		outNum = list(map(int,str(number))) #입력값 리스트로 담는다.
		threadFlag = True #새로운 스레드 실행플레그
		thread.start()
except KeyboardInterrupt:
	GPIO.cleanup()
</code>
</pre>

- 시연<br>
 ![이미지1](https://github.com/JongWon112/RaspberryPi/blob/main/images/fndImg1.jpg) <br>
 ![이미지2](https://github.com/JongWon112/RaspberryPi/blob/main/images/fndImg2.jpg) <br>
 ![이미지3](https://github.com/JongWon112/RaspberryPi/blob/main/images/fndImg3.jpg) <br>
 
