import sys
import socket
from threading import Thread
BUFSIZE = 1024
userList = [] # 현재 접속중인 유저 리스트
def run_server(port):
#	BUFSIZE = 1024
	userNo = 1
	global userList
	host = socket.gethostname()
	ip = socket.gethostbyname(host)
	serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv.bind((host, int(port)))
	serv.listen(5)
	print("server %s : %s start...." %(ip, port))
	while True:
		clnt,addr = serv.accept()
		if(clnt and addr): #접속 요청이 발생하면
			print("%s client connected..." %clnt)
			th = Thread(target=chatThread,args=(clnt,userNo)).start()
			userList.append([clnt, th])
			userNo += 1
#			Thread(target = chatThread, args = (clnt,)).start()

def chatThread(clnt, userNo):
	global BUFSIZE
	global userList
	while True:
		data = clnt.recv(BUFSIZE)
		print("%s : %s" % ("user" +str(userNo), data.decode()))
		if data.decode() == 'bye':
			clnt.close()
			for ths in userList:
				if ths[0] == clnt:
					ths[1].join()
		#모든 유저에게 입력된 메세지를 보내준다.
	#	for i in userList:
	#		if i != clnt: #본인이 보낸 메세지 제외
	#			msg = "%s : %s" % ("user" + str(userNo), data.decode())
	#			i.send(bytes(msg.encode()))
	#		else:
	#			pass
		clnt.sendall(data)

if __name__ == '__main__':
	try:
		run_server(sys.argv[1])
	except (IndexError, NameError) as e:
		print("Execute: %s <port>" % sys.argv[0])
