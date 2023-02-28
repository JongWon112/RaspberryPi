import RPi.GPIO as GPIO
import time

piezoPin = 13
do = 523
le = 587
me = 659
pa = 698
sol = 784
la = 880
si = 988
do_ = 1046
melody = [sol, sol, la, la, sol, sol, me,
			sol, sol, me, me, le,
			sol, sol, la, la, sol, sol, me,
			sol, me, le, me, do]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

s = GPIO.PWM(piezoPin, 1000)

try:
	while True:
		s.start(50) # PWD start 
		for i in range(len(melody)):
			s.ChangeFrequency(melody[i])
			time.sleep(0.5)
		s.stop()	#PWM stop
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
