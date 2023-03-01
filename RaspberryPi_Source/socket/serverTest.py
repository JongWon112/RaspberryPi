# 1회 Echo server

import socket
import time

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufsize = 1024
port = 8080
s_name = socket.gethostname()
serversock.bind((s_name, port))
serversock.listen(1)

clientsock, address = serversock.accept()
print("connect...")
receive_data = clientsock.recv(bufsize)
print("recv data: %s" % receive_data.decode())

clientsock.send(receive_data)

time.sleep(1)
clientsock.close()
serversock.close()
