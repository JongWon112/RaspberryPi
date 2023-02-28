import RPi.GPIO as GPIO
import time
import getch

piezoPin = 13
do = 523
le = 587
me = 659
pa = 698
sol = 784
la = 880
si = 988
do_ = 1046

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

s = GPIO.PWM(piezoPin, 1000)

try:
	while True:
		ch = getch.getch()
		print(ch)
		if ch not in ['a','s','d','f','g','h','j','k','A','S','D','F','G','H','J','K']:
			continue
		if(ch == 'a'):
			s.ChangeFrequency(do)
		elif(ch == 's'):
			s.ChangeFrequency(le)
		elif(ch == 'd'):
			s.ChangeFrequency(me)
		elif(ch == 'f'):
			s.ChangeFrequency(pa)
		elif(ch == 'g'):
			s.ChangeFrequency(sol)
		elif(ch == 'h'):
			s.ChangeFrequency(la)
		elif(ch == 'j'):
			s.ChangeFrequency(si)
		elif(ch == 'k'):
			s.ChangeFrequency(do_)
		s.start(50)
		time.sleep(0.3)
		s.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
