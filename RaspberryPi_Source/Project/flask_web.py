from flask import Flask
import pymysql

dataList = []

app = Flask(__name__)

def getDb():
	conn = pymysql.connect(host='localhost', user='root', db='mydb',
						password='1234', charset='utf8')
	query = 'SELECT * FROM temp_humi'
	with conn:
		with conn.cursor() as cur:
			cur.execute(query)
			result = cur.fetchall()
			for data in result:
				dataList.append(data)
	return dataList
		
@app.route('/')
def home():
	str = '''
		<!DOCTYPE HTML><html>
		<head>
			<title>Flask temp_humi</title>
		</head>
		<body>
			<h1>temp, humi</h1>
	 '''
	dataList = getDb()
	for data in dataList:
		str += f'<p>NO : {data[0]}  temp : {data[1]}  humi : {data[2]}</p>'

	str += ''' </body>
		</html>'''
	return str

if __name__ == '__main__':
	app.run(host='192.168.0.59', port='9090', debug=True)
