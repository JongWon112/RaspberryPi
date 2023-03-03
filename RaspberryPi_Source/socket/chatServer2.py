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
	serv.bind((host, int(port)))
	serv.listen(5)
	print("server %s : %s start...." %(ip, port))
	while True:
		clnt,addr = serv.accept()
		if(clnt and addr): #접속 요청이 발생하면
			print("%s client connected..." %clnt)
			#최초 접속시 수신된 아이디를 받는다.
			Client_Id = clnt.recv(BUFSIZE).decode()
			clients.append([clnt,Client_Id])
			Thread(target=chatThread,args=(clnt, Client_Id)).start()


def chatThread(clnt, Client_Id):
	global BUFSIZE
	global clients
	while True:
		data = clnt.recv(BUFSIZE)
		print("%s : %s" % (Client_Id, data.decode()))
		if data.decode() == 'bye':
			clients.remove([clnt, Client_Id])
			#rIndex = clients.index(clnt)
			#clients.remove(rIndex)
			clnt.close()
			return
		#본인 제외 다른 클라이언트에게 전송
		for client in clients:
			# print("sendClient : ", clnt, "send2Client", client)
			if clnt != client[0]:
				# print("send!!!")
				outStr = Client_Id + " : " + data.decode()
				client[0].sendall(outStr.encode())

if __name__ == '__main__':
	try:
		run_server(sys.argv[1])
	except (IndexError, NameError) as e:
		print("Execute: %s <port>" % sys.argv[0])
