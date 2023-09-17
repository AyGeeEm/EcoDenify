import requests

api_key = '890d59fb54fe5c2415fb83a495bf833026b3336c52539227302503861a215595'  # Replace with your actual API key
query = 'OpenAI'

# Define the search engine (e.g., Google)
search_engine = 'google'

def get_user_city():
    try:
        # Send a request to ipinfo.io to get geolocation information based on the user's IP address
        response = requests.get('https://ipinfo.io')

        # Parse the JSON response
        data = response.json()

        # Extract the city from the response
        city = data.get('city', 'Unknown')

        return city
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'Unknown'


# JUST USE THIS FOR TESTING THE LOCATION OF USER
if __name__ == '__main__':
    user_city = get_user_city()
    print(f"Your approximate city is: {user_city}")


def getModelSearches():

    modelNum = input("please input the model Number\n")
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
        for result in results:
            print(f'Title: {result["title"]}')
            print(f'Link: {result["link"]}\n')
    else:
        print(f'Error: Unable to fetch search results. Status code: {response.status_code}')

getModelSearches()
