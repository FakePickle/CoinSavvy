import requests
import csv
from datetime import datetime

# API endpoint and parameters
api_url = "https://min-api.cryptocompare.com/data/v2/histoday"
api_key = "2b44f1fc466577cb553820b4d1221ec1eab50ad4877b3ebfe79d1166da476f61"  # Replace with your actual CryptoCompare API key
fsym = "BTC"
tsym = "USD"
limit = 1461  # Adjusted limit for the desired period (1461 days)
toTs = 1643673600  # Unix timestamp for 2022-01-31
fromTs = 1514764800  # Unix timestamp for 2018-01-01

# Construct the API request URL with both fromTs and toTs
url = f"{api_url}?fsym={fsym}&tsym={tsym}&limit={limit}&toTs={toTs}&fromTs={fromTs}&api_key={api_key}"

# Make the API request
response = requests.get(url)
data = response.json()
data = data["Data"]["Data"]
# Print the formatted data
# Additional options:
# - Save the data to a CSV file: df.to_csv("btc_historical_data.csv")
# - Perform further analysis or visualization using pandas

if response.status_code == 200:
    with open("btc_historical_data.csv", mode="w", newline="") as csv_file:

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['time', 'open', 'high', 'low', 'close', 'volumeto'])

        for row in data:
            csv_writer.writerow([
                datetime.utcfromtimestamp(row['time']).strftime('%Y-%m-%d %H:%M:%S'),
                row['open'],
                row['high'],
                row['low'],
                row['close'],
                row['volumeto'],
                # row['conversionType'],
                # row['conversionSymbol']
            ])


  