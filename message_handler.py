from datetime import datetime
from weather import *
import json


def respond_to_message (received_message):
# figure out if this is a "join" or a "message" and respond accordingly.
	
	if (received_message['action'] == 'join'):
		response_json = jsonify_single_text_response("Hello " + received_message['name'] + "!")

	elif (received_message['action'] == 'message'):
		response = draft_response(received_message['text'])
		response_json = jsonify_single_text_response(response)

	else:
		response_json = jsonify_single_text_response("Error: the JSON your browser sent is in the wrong format.")

	return (response_json)

def jsonify_single_text_response(response_text):
# Convert a response string into the JSON required by the Lessenger client.
# This method only proceduces single-part text responses.

	response_dict = {}
	response_dict['messages'] = []
	
	message = {}
	message['type'] = "text"
	message['text'] = response_text
	response_dict['messages'].append(message)
	response_json = json.dumps(response_dict)
	return (response_json)


def draft_response (user_message):
# Given a chat message from the user, draft our reply to be sent back.
	
	user_message = user_message.lower()

	# what's the weather in <Location> OR weather in <Location>
	if ("weather in " in user_message):
		place = user_message.split("weather in ")[1]
		response = get_weather_report(place)

	# <Location> weather
	elif (" weather" in user_message) :
		place = user_message.split(" weather")[0]
		response = get_weather_report(place)

	# any other message, e.g., "I like kittens."
	else:
		response = "Yes. I am a robot."

	return (response)