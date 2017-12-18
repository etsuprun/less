from api_keys import *
import googlemaps # wrapper for Google maps
import forecastio # wrapper for Dark Sky API


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
