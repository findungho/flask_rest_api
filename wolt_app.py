# Backend Summer 2020 Engineering Internship
# Option 2
# Create a REST API endpoint that allows searching restaurants. 
# The API endpoint need 3 parameters: query string (_q_), latitude of customer's location (_lat_) and longtitue of customer's location (_lon_).
# Author : Dung Ho


import math
from flask import Flask, request, json, jsonify

#Create the Flask application
app = Flask(__name__)


##-----------------------------------------------------------------------------------------------
##SECTION: Main code
##-----------------------------------------------------------------------------------------------

#List all the restaurants from JSON file
with open('restaurants.json') as f:
	restaurants = (json.load(f)).get('restaurants')


#Function calculates distance between two locations by applying Harvesine fomurla
#https://en.wikipedia.org/wiki/Haversine_formula
def haversine(origin, destination):
	org_lat, org_lon = origin
	des_lat, des_lon = destination
	radius = 6371 # Km -  Radius of the Earth
	
	#Distance between latitudes and longtitudes (in radians)
	d_lat = math.radians(des_lat - org_lat)
	d_lon = math.radians(des_lon - org_lon)
	
	#Convert latitudes to radians
	r_lat1 = math.radians(org_lat)
	r_lat2 = math.radians(des_lat)
	
	#Apply Haversine fomurla to calculate distance between 2 locations
	a = pow(math.sin(d_lat/2), 2) + math.cos(r_lat1)*math.cos(r_lat2)*pow(math.sin(d_lon/2), 2)
	
	#Distance
	d = 2 * radius * math.asin(math.sqrt(a))

	return d


#Function returns the restaurats that offer the food's keyword
def get_restaurant(food_name, lat, lon, restaurants):
	#Create empty list to store the restaurants after search
	list_restaurants = []
	for restaurant in restaurants:
		if food_name in restaurant['name'] or food_name in restaurant['description'] or food_name in restaurant['tags']:
			distance = haversine([lat, lon], restaurant['location'][::-1])
			#If the restaurant closer than 3km from the customer's location then add to the list
			if distance <= 3:
				list_restaurants.append(restaurant)
			else: 
				return "No restaurant found!!!"
				
	return list_restaurants



##-----------------------------------------------------------------------------------------------
##SECTION: API Endpoints
##-----------------------------------------------------------------------------------------------

#Handling error
@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404


#Show Homepage
@app.route('/')
@app.route('/index')
def index():
	return """<h1> WOLT SUMMER INTERNSHIP 2020</h1>
		           <p> Search Restaurant base on the food types and the customer's location. </p>"""


#API endpoint - Show all the restaurants in Helsinki
@app.route('/restaurants/all', methods = ['GET'])
def res():
	return jsonify(restaurants)
	

# API Endpoint - Perform search the restaurant base on food's name and customer's location	
@app.route('/restaurants/search', methods = ['GET'])
def search():
	# Check if a query was provided as part of the URL.
	# If the query is provided, assign it to a variable.
	# If no query field is provided, display an error in the browser.
	query_parameters = request.args
	query = query_parameters.get('q')
	latitude = query_parameters.get('lat', type = float)
	longitude = query_parameters.get('lon', type = float)
	
	#Return the list of restaurants that matched the query
	l_restaurants = get_restaurant(query, latitude, longitude, restaurants)
	
	if len(query) < 1 or query == None:
		return "Error: No query field provided. Please specify a query."
	else:
		return jsonify(l_restaurants)
	
	
#Run the application and start the debug	
if __name__ == "__main__":
	app.run(debug=True)