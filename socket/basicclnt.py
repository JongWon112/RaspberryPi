import socket

#소켓 생성(주소 체계 : IPv4, 데이터유형: TCP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#접속 시도(server IP, port)
sock.connect(("127.0.1.1", 8080))

#data 송신
#encode -> binary 타입으로 변환
sock.sendall("Hi Python socket programming".encode())

#접속 종료
sock.close()
