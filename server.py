from flask import request, Flask
from flask_cors import CORS
from message_handler import *

app = Flask(__name__)
CORS(app)

@app.route('/chat/messages', methods=['POST'])
@app.route('/chat/message', methods=['POST'])

def handle_message():
	
	received_message = request.form.to_dict()
	response = respond_to_message(received_message)
	return (response)

app.run(host = '0.0.0.0', port = 9000)