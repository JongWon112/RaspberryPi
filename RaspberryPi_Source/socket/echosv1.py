# port 설정
import sys
import socket

def run_server(port = (sys.argv[1])):
	#with -> with 구문이 끝나면 서버 소켓이 자동적으로 닫힌다.
	with socket.socket() as serv:
		print(socket.gethostname())
		serv.bind((socket.gethostname(), int(port)))
		serv.listen(1)
		print("server start...")
		clnt, addr = serv.accept()
		print("client connected..")
		while True:
			data = clnt.recv(1024)
			print("recv data : %s" % data.decode())
			clnt.sendall(data)
		clnt.close()

if __name__ == '__main__':
	run_server()
