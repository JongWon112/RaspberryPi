import Adafruit_DHT
import time
import pymysql

#전역변수 선언
conn = None
cur = None

query = ""

dht = Adafruit_DHT.DHT11

dhtPin = 14

conn = pymysql.connect(host = 'localhost', user='root', db='mydb',
						 password='1234', charset='utf8')
cur = conn.cursor()

try:
	while True:
		humi, temp = Adafruit_DHT.read_retry(dht, dhtPin)
		if humi is not None and temp is not None:
			temp = "%.1fC"  %temp
			humi = "%.1f%%" %humi
			#print("Temp ",temp,"HUMI ",  humi)
			query = "INSERT INTO temp_humi (temp, humi) values('%s', '%s')" %(temp, humi) 
			cur.execute(query)
			conn.commit()
		else:
			print("Failed to get reading. Try again!!")
		time.sleep(1)
except Exception as e:
	print(e)
finally:
	conn.close()


