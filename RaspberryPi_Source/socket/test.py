import sys

def test(port=sys.argv[1]): #python 실행시 파라미터
							#0번 인덱스는 실행할  파일 이름 이후부터는 던져주는 파라미터
	print(port, int(port))
#	print(port)

if __name__ == '__main__':
	test()
