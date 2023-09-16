import requests

api_key = '890d59fb54fe5c2415fb83a495bf833026b3336c52539227302503861a215595'  # Replace with your actual API key
query = 'OpenAI'


#serialNum = int(input("Please Input the serial Number"))
modelNum = input("please input the model Number")
#let me know if you see this


# Define the search engine (e.g., Google)
search_engine = 'google'

# Construct the URL for the API request
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