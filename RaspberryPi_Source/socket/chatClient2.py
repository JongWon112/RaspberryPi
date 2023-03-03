import sys
import socket
from threading import Thread
BUFSIZE = 1024
runFlag = False
def getEchoData(clnt):
	global runFlag
	print("echoThread 시작")
	while True:
		if(runFlag == False):
			print("echoThread 종료")
			return
		echoData = clnt.recv(BUFSIZE)
		print(echoData.decode())
	

def run_client(host, port, id):
	global runFlag
	clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clnt.connect((host, int(port)))
	#최초 연결시 접속 id를 보낸다.
	clnt.sendall(id.encode())
	#echoData를 받는 스레드 실행...
	Thread(target=getEchoData, args=(clnt,)).start()
	while True:
		runFlag = True

		
		# sendData = input('ME >> ')
		sendData = input('')
		clnt.sendall(sendData.encode())
		if sendData == 'bye':
			break
		
		
		# if(clnt.recv(BUFSIZE)):
		# 	echoData = clnt.recv(BUFSIZE)
		# 	print(echoData.decode())
	clnt.close()
	runFlag = False

if __name__ == '__main__':
	try:
		run_client(sys.argv[1], sys.argv[2], sys.argv[3]) #3번째 인자는 접속할 id 입력...
	except (IndexError, NameError) as e:
		print("Exec : %s <IP> <port>" % sys.argv[0])

