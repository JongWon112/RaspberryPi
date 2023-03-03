import Adafruit_DHT
import time

dht = Adafruit_DHT.DHT11

dhtPin = 14

while True:
	humi, temp = Adafruit_DHT.read_retry(dht, dhtPin)
	if humi is not None and temp is not None:
		print("Temp=%.1fC Humi=%.1f%%" %(temp, humi))
	else:
		print("Failed to get reading. Try again!!")
	time.sleep(1)
