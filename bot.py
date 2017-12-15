import googlemaps
import forecastio
from datetime import datetime
from api_keys import *


gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# Geocoding an address

def get_weather(place):

	geocode_result = gmaps.geocode(place)
	coordinates = geocode_result[0]['geometry']['location']

	forecast = forecastio.load_forecast(DARK_SKY_API_KEY, coordinates['lat'], coordinates['lng'])
	print (coordinates)
	print (forecast.currently())

if __name__ == '__main__':
	get_weather('RSW')