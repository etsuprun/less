import googlemaps
import forecastio # wrapper for Dark Sky API
from datetime import datetime
from api_keys import *


gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)


def get_weather_report(place):
# Given a string containing the name of a place (address, ZIP code, city, etc.), return the current weather report.
# We first geocode the place using the Google Maps API and then fetch the weather using Dark Sky API.

	geocode_result = gmaps.geocode(place)
	coordinates = geocode_result[0]['geometry']['location']


	forecast = forecastio.load_forecast(DARK_SKY_API_KEY, coordinates['lat'], coordinates['lng'], units="us")
	current_weather = forecast.currently()
	temperature_str = str(round(current_weather.temperature))

	report = "Right now, it's " + temperature_str + " degrees Fahrenheit. " + current_weather.summary + "."
	return (report)

def draft_response(user_message):
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