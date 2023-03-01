import socket

#socket -> bind -> listen -> accept

# 소켓 생성(주소체계 : IPv4, 데이터유형 : TCP)
# AF_INET -> 주소체계 IPv4를 의미, SOCK_STREAM -> TCP를 의미
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# ip = socket.gethostbyname(host)
# 주소할당(host, port)
sock.bind(("", 8080))
# 접속 대기
sock.listen()
# 접속 수락
c_sock, addr = sock.accept()
# data 송신
receive_data = c_sock.recv(1024)
print("recv data: %s" %receive_data.decode())
#접속 종료
c_sock.close() #클라이언트 소켓 종료
sock.close()  # 서버 소켓 종료

