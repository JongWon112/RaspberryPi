import time
from threading import Thread

def inc_func1():
	i = 0
	while True:
		print("inc_func1() i : %d" % i)
		time.sleep(1)
		i += 1

def inc_func2():
	i = 0
	while True:
		print("inc_func2() i : %d" % i)
		time.sleep(2)
		i += 1

def main():
	try:
		th1 = Thread(target = inc_func1, args = ())
		th2 = Thread(target = inc_func2, args = ())
		th1.start() # thread start
		th2.start()
	except KeyboardInterrupt:
		th1.join() # thread 종료
		th2.join()

if __name__ == '__main__':
	main()
