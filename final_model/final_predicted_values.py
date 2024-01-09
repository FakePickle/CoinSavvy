import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import csv
import matplotlib.pyplot as plt

# Load the dataset using pandas
data = pd.read_csv('datasets/training_dataset.csv')
data_test = pd.read_csv('datasets/testing_dataset.csv')

X_features = ['open', "volumeto"]
target_column = 'close'

# Extract features (X_train) and target (y_train)
X_train = data[X_features]
y_train = data[target_column]

# Split the data into training and testing sets
X_test = data_test[X_features]
y_test = data_test[target_column]

linear_model = LinearRegression()
linear_model.fit(X_train, y_train) 

predictions = linear_model.predict(X_test).tolist()

with open("datasets/final_predicted_values.csv", mode="w", newline="") as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['time', 'open', 'volumeto', 'predicted_close', 'close'])
    
    for index, row in data_test.iterrows():  # Use iterrows to iterate through DataFrame rows
        time = row['time']
        open_val = row['open']
        volumeto = row['volumeto']
        predicted_close = predictions[index]
        close = row['close']

        csv_writer.writerow([time, open_val, volumeto, predicted_close, close])

mse_train = mean_squared_error(y_test, predictions)
mse_test = mean_squared_error(y_train, linear_model.predict(X_train))
print(f"Mean Squared Error on Training Set: {mse_train}")
print(f"Mean Squared Error on Test Set: {mse_test}")


time_column =data_test['time']

# Plotting the actual values
plt.figure(figsize=(10, 6))
plt.plot(time_column, y_test, label='Actual', marker='o')

# Plotting the predicted values
plt.plot(time_column, predictions, label='Predicted', marker='x')
plt.show()