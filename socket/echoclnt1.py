import sys
import socket

def run_client(host=sys.argv[1], port=sys.argv[2]):
	with socket.socket() as clnt:
		clnt.connect((host, int(port)))
		while True:
			sendData = input("send message >> ")
			clnt.sendall(sendData.encode())
			echoData = clnt.recv(1024)
			print("echo data : %s" % echoData.decode())

if __name__ == "__main__":
	run_client()
