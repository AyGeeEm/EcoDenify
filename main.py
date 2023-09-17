from flask import Flask
from serpapi import GoogleSearch
import requests
import os

api_key = '890d59fb54fe5c2415fb83a495bf833026b3336c52539227302503861a215595'  # Replace with your actual API key
query = 'OpenAI'
app = Flask(__name__)

# Define the search engine (e.g., Google)
search_engine = 'google'

@app.route('/')
def index():
    return 'server works'

@app.route('/user/<modelNum>')

def get_user_location(modelNum):
    try:
        # Send a request to ipinfo.io to get geolocation information based on the user's IP address
        response = requests.get('https://ipinfo.io')

        # Parse the JSON response
        data = response.json()

        # Extract the city and state from the response
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')

        return city, state
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'Unknown', 'Unknown'

# Retrieves information on top search results for cpu model number
def getModelSearches(modelNum):
    try:
        # Convert to integer if possible
        url = f'https://serpapi.com/search.json?q={modelNum}&engine={search_engine}&api_key={api_key}'
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Access the search results
            results = data['organic_results']

            # Print the titles and links of the results
            if results:
                first_result = results[0]
                print(f'Title: {first_result["title"]}')
                print(f'Link: {first_result["link"]}\n')
            else:
                print("No search results found.")

        user_city, user_state = get_user_location()
        url = f'https://serpapi.com/search.json?q="electronic+waste"&location={user_city, user_state}&engine=google&api_key={api_key}'

        # Send the request to SERP API
        response = requests.get(url)

        # Parse the JSON response
        data = response.json()

        # Process and extract Local Pack results
        if 'local_results' in data:

            results = data['local_results']

            # print(results['places'][0]['rating'])
            for result in results['places']:
                print(result['title'])
                print(result['address'])
                if 'rating' in result:
                    print(result['rating'])
                else:
                    print("No rating available")
        else:
            print("No Local Pack results found.")

    except ValueError:
        return "Invalid model number (not an integer)"

# Retrieves information on local e-waste deposits
# def get_final_location():


    # SCRAPPED FOR NOW

    # Construct the API request URL




'''if __name__ == '__main__':
    user_city, user_state = get_user_location()
    print(f"Your approximate location is: {user_city}, {user_state}")
    # get_final_location()'''

get_user_location()
getModelSearches()