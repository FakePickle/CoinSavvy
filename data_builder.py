import requests
import csv
from datetime import datetime

# API endpoint and parameters
api_url = "https://min-api.cryptocompare.com/data/v2/histoday"
api_key = "2b44f1fc466577cb553820b4d1221ec1eab50ad4877b3ebfe79d1166da476f61"  # Replace with your actual CryptoCompare API key
fsym = "BTC"
tsym = "USD"
limit = 1461 # 1461 days = 4 years
toTs = 1672516800
fromTs = 1514764800 

# Construct the API request URL with both fromTs and toTs
url = f"{api_url}?fsym={fsym}&tsym={tsym}&limit={limit}&toTs={toTs}&fromTs={fromTs}&api_key={api_key}"

# Make the API request
response = requests.get(url)
data = response.json()
data = data["Data"]["Data"]

if response.status_code == 200:
    with open("new_dataset.csv", mode="w", newline="") as csv_file:

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['time', 'open', 'high', 'low', 'close', 'volumeto'])

        for row in data:
            csv_writer.writerow([
                datetime.utcfromtimestamp(row['time']).strftime('%Y-%m-%d'),
                row['open'],
                row['high'],
                row['low'],
                row['close'],
                row['volumeto']
            ])