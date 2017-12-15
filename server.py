from flask import Flask
app = Flask(__name__)

@app.route('/test')
def hello_world():
	return 'Hello, World!'

@app.route('/chat/message', methods=['POST'])
def handle_message():
	return 'Hello, World!'

