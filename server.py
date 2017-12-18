from flask import request, Flask
from flask_cors import CORS
from message_handler import *
import sys

app = Flask(__name__)
CORS(app)

@app.route('/chat/messages', methods=['POST'])
@app.route('/chat/message', methods=['POST'])

def handle_message():
	
	received_message = request.form.to_dict()
	sys.stderr.write(str(received_message))
	response = respond_to_message(received_message)
	return (response)

app.run(port = 9000)