import time
import threading
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
		time.sleep(1)
		i += 1

if __name__ == "__main__":
	thread1 = threading.Thread(target = inc_func1)
	thread1.start()
	thread2 = threading.Thread(target = inc_func2)
	thread2.start()
#	inc_func1()
#	inc_func2()
