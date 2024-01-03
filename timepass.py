import requests
import csv


for _ in range(1,13):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&month=2018-0{_}&outputsize=full&apikey=KY07Z1XZGQSO9ITA'

    r = requests.get(url)
    with open(f'data{_}.csv', 'w') as f:
        writer = csv.writer(f)
        for line in r.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))