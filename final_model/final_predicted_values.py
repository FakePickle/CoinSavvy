import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import csv
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "BTC-USD"
start_date = "2018-02-01"
end_date = "2022-01-01"

# Download historical data
data = yf.download(ticker, start=start_date, end=end_date)
data_test = yf.download(ticker, start="2022-02-01", end="2023-01-01")


X_features = ['Open', "Volume"]
target_column = 'Close'

# Extract features (X_train) and target (y_train)
X_train = data[X_features]
y_train = data[target_column]

# Split the data into training and testing sets
X_test = data_test[X_features]
y_test = data_test[target_column]

linear_model = LinearRegression()
linear_model.fit(X_train, y_train) 

predictions = linear_model.predict(X_test).tolist()
time_column = data_test.index.tolist()


with open("../datasets/final_predicted_values.csv", mode="w", newline="") as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Date', 'Open', 'Volume', 'Predicted Close', 'Actual Close'])
    index = 0
    for date, row in data_test.iterrows():  # Use iterrows to iterate through DataFrame rows
        open_val = row['Open']
        volumeto = row['Volume']
        predicted_close = predictions[index]
        close = row['Close']

        csv_writer.writerow([date, open_val, volumeto, predicted_close, close])
        index+=1

mse_train = mean_squared_error(y_test, predictions)
mse_test = mean_squared_error(y_train, linear_model.predict(X_train))
print(f"Mean Squared Error on Training Set: {mse_train}")
print(f"Mean Squared Error on Test Set: {mse_test}")



# Plotting the actual values
plt.figure(figsize=(10, 6))
plt.title('Actual vs Predicted Close Values')
plt.plot(time_column, y_test, label='Actual', marker='o')

# Plotting the predicted values
plt.plot(time_column, predictions, label='Predicted', marker='x')
plt.show()