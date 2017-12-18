import googlemaps
import forecastio # wrapper for Dark Sky API
from datetime import datetime
from api_keys import *
import json


def respond_to_message (received_message):
	
	if (received_message['action'] == 'join'):
		response_json = jsonify_single_text_response("Hello " + received_message['name'] + "!")

	elif (received_message['action'] == 'message'):
		response = draft_response(received_message['text'])
		response_json = jsonify_single_text_response(response)

	else:
		response_json = jsonify_single_text_response("Error: the JSON your browser sent is in the wrong format.")

	return (response_json)

def jsonify_single_text_response(response_text):

	response_dict = {}
	response_dict['messages'] = []
	
	message = {}
	message['type'] = "text"
	message['text'] = response_text
	response_dict['messages'].append(message)
	response_json = json.dumps(response_dict)
	return (response_json)


def get_weather_report (place):
# Given a string containing the name of a place (address, ZIP code, city, etc.), return the current weather report.
# We first geocode the place using the Google Maps API and then fetch the weather using Dark Sky API.

	gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
	geocode_result = gmaps.geocode(place)
	coordinates = geocode_result[0]['geometry']['location']


	forecast = forecastio.load_forecast(DARK_SKY_API_KEY, coordinates['lat'], coordinates['lng'], units="us")
	current_weather = forecast.currently()
	temperature_str = str(round(current_weather.temperature))

	report = "Right now, it's " + temperature_str + " degrees Fahrenheit. " + current_weather.summary + "."
	return (report)

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

if __name__ == '__main__':
	user_message = draft_response("what's the weather in Naples FL")
	print (user_message)
	user_message = draft_response('Naples weather')
	print (user_message)
	user_message = draft_response('Naples')
	print (user_message)