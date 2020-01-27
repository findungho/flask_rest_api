													WOLT - SUMMER INTERN 2020

# Summer 2020 Internships - Engineering Pre-assignment

_This is a mandatory pre-assignment task for Wolt's engineering intern positions. Read more about our summer jobs in 2020 [here](https://www.wolt.com)._

## In short

1. Select either frontend or backend version of this assignment. **No need to do both of them**.
2. Solve the task. When you are ready, leave us a frontend application [here](https://jobs.lever.co/wolt/7fbb1572-6697-4e9d-b6ba-0e316ecb9cc1) **or** a backend application [here](https://jobs.lever.co/wolt/7d18a18f-1a28-48a6-ab69-a17327466675). Attach source codes as a zip-file to the application form.
3. That's it! We will get back to you.

## Overview

A list of restaurants is an important element in Wolt app. Depending on where our customers are located, they will be able to order food from few dozen or even from hundreds of different restaurants. Views in the app (_Discovery, Search, Delivers, Nearby_) sort restaurants based on the delivery time, popularity, rating and various other factors when trying to find the most relevant matches for each customer.  

Your task is to either display a list of restaurant using the given data set ([Option 1](#option1)) **OR** create an API that allows searching restaurants from the data set ([Option 2](#option2)).

Fun fact: the data set contains real Wolt restaurants, so we actually use a very similar json-format internally.

## Restaurant data

_restaurant.json_ contains fifty restaurants from central Helsinki area. Each object has a set fields providing more information about the restaurant, like _name_, _image_ and _location_. 

Example:

	{
		"city": "Helsinki",
		"currency": "EUR",
		"delivery_price": 390,
		"description": "Japanilaista ramenia parhaimmillaan",
		"image": "https://prod-wolt-venue-images-cdn.wolt.com/5d108aa82e757db3f4946ca9/d88ebd36611a5e56bfc6a60264fe3f81",
		"location": [
			24.941786527633663,
			60.169934599421396
		],
		"name": "Momotoko Citycenter",
		"online": false,
		"tags": [
			"ramen",
			"risotto"
		],
		"blurhash": "j2DUFG8jbu8AXuLIT5Tt0B01R2;;",
	}

Fields: 

- _city_ : A city where the restaurant is located (type: _string_)
- _currency_: ISO 4217 code of the currency the restaurant is using (type: _string_)
- _delivery price_: Delivery cost from the restaurant to a customer. The price is stored as subunits, so 390 in this case would be 3.90€ (type: _integer_)
- _description_: More information about what kind of restaurant it is (type: _string_)
- _image_: A link to restaurant's image (type: _string_)
- _location_: Restaurant's location in latitude & longitude coordinates. First element in the list is the longitude (type: a list containing two decimal elements)
- _name_: The name of the restaurant (type: _string_)
- _online_: If _true_, the restaurant is accepting orders at the moment. If _false_, then ordering is not possible (type: _boolean_)
- _tags_: A list of tags describing what kind of food the restaurant sells, e.g. pizza / burger (type: a list of strings, max.  3 elements)
- _blurhash_ : See [bonus task](#bonus)

<a name="option2"></a>
## Option 2) Backend task - search
Create a REST API endpoint that allows searching restaurants. API needs to accept three parameters:
- _q_: query string. Full or partial match for the string is searched from _name_, _description_ and _tags_ fields. A minimum length for the query string is one character.
- _lat_: latitude coordinate (customer's location)
- _lon_ : longitude coordinate (customer's location)

API should return restaurant (objects) which **match the given query string** and are **closer than 3 kilometers** from coordinates. 

Example query:

	/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
	
This search would return restaurants (in JSON format) which contain a word _sushi_ and are closer than 3km to the point [60.17045, 24.93147]. 

## How to run?

Requirements: Python3, Flask

1. Clone at https://github.com/findungho/wolt_summer2020.git
Or download zip file.
2. Extract zip file. 
3. Open Termianl (MacOS & Linux) or CMD (Windows) and navigate to "wolt_summer2020" folder
4. Run with command "python3 wolt_app.py"

