# The program retrieves the Exchequer Account (Historical Series) dataset from CSO 
# and saves it as 'cso.json' without modifying the data.
# Author: Tomasz Uszynski

import requests

# CSO API URL for the dataset
url = 'https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D'

# Make a GET request to the CSO API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open('cso.json', 'w') as file:
        file.write(response.text)
else:
    print(f'Failed to retrieve data: {response.status_code}')
