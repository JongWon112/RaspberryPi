from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
   # app.run(debug=True)
	app.run(host='192.168.0.59', port = '9090', debug = True)
