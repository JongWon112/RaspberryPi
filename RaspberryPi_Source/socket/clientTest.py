#Echo client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufsize = 1024
port = 8080
c_name = socket.gethostname()
client.connect((c_name, port))

name = input("Who are You?")
#client.send(bytes(name, 'utf-8'))
client.send(name.encode())

print("echo : %s" % client.recv(1024).decode())

client.close()
