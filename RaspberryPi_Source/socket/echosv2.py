# 5 client 순차적으로 연결
import sys
import socket

def run_server(port):
	BUFSIZE = 1024
	host = socket.gethostname()
	ip = socket.gethostbyname(host)
	serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv.bind((host, int(port)))
	serv.listen(5) #접속 클라이언트의 수 설정
	print("server %s : %s start..." % (ip, port))

	for i in range(1, 6):
		clnt, addr = serv.accept()
		print("%d client connected..." % i)
		while True:
			data = clnt.recv(BUFSIZE)
			print("recv from %d : %s" % (i, data.decode()))
			if data.decode() == 'bye':
				clnt.close()
				break
			clnt.sendall(data)
		#clnt.close()
	serv.close()

if __name__ == '__main__':
	try:
		run_server(sys.argv[1])
	except (IndexError, NameError) as e:
		print("Execute: %s <port>" % sys.argv[0])

