import requests
import csv
from datetime import datetime

# API endpoint and parameters
api_url = "https://min-api.cryptocompare.com/data/v2/histoday"
api_key = "2b44f1fc466577cb553820b4d1221ec1eab50ad4877b3ebfe79d1166da476f61"  # Replace with your actual CryptoCompare API key
fsym = "BTC"
tsym = "USD"
limit = 1491
toTs = 1643653800
fromTs = 1514745000 

# Construct the API request URL with both fromTs and toTs
url = f"{api_url}?fsym={fsym}&tsym={tsym}&limit={limit}&toTs={toTs}&fromTs={fromTs}&api_key={api_key}"

# Make the API request
response = requests.get(url)
data = response.json()
data = data["Data"]["Data"]

if response.status_code == 200:
    # Replace #dataset.csv with "datasets\training_dataset.csv" or "datasets\testing_dataset.csv" depending on which dataset you are building
    with open("dataset.csv", mode="w", newline="") as csv_file:

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