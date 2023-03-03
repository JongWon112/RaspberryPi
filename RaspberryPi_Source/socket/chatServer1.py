import sys
import socket
from threading import Thread
BUFSIZE = 1024
clients = [] # 현재 접속중인 유저 리스트
def run_server(port):
#	BUFSIZE = 1024
	global clients
	host = socket.gethostname()
	ip = socket.gethostbyname(host)
	serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv.bind((ip, int(port)))
	serv.listen(5)
	print("server %s : %s start...." %(ip, port))
	while True:
		clnt,addr = serv.accept()
		if(clnt and addr): #접속 요청이 발생하면
			print("%s client connected..." %clnt)
			Thread(target=chatThread,args=(clnt,)).start()
			clients.append(clnt)

def chatThread(clnt):
	global BUFSIZE
	global clients
	while True:
		data = clnt.recv(BUFSIZE)
		print("%s" % data.decode())
		if data.decode() == 'bye':
			clnt.close()
		clnt.sendall(data)

if __name__ == '__main__':
	try:
		run_server(sys.argv[1])
	except (IndexError, NameError) as e:
		print("Execute: %s <port>" % sys.argv[0])
