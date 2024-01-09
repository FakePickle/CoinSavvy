import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import csv

# Load the dataset using pandas
data = pd.read_csv('datasets/training_dataset.csv')
open_value_start = 38721.49

# Model that predicts high value based on open value
X_features1 = ['open']
target_column1 = 'high'

X_train1 = data[X_features1]
y_train1 = data[target_column1]

high_predictor_model = LinearRegression()
high_predictor_model.fit(X_train1, y_train1) 

# Model that predicts low value based on open and high values
X_features2 = ['open','high']
target_column2 = 'low'

X_train_2 = data[X_features2]
y_train_2 = data[target_column2]

low_predictor_model = LinearRegression()
low_predictor_model.fit(X_train_2, y_train_2)

# Model that predicts volumeto value based on open, high and low values
X_features3 = ['open','high','low']
target_column3 = 'volumeto'

X_train_3 = data[X_features3]
y_train_3 = data[target_column3]

volume_predictor_model = LinearRegression()
volume_predictor_model.fit(X_train_3, y_train_3)

# Model that predicts close value based on open, high, low and volumeto values
X_features4 = ['open','high','low','volumeto']
target_column4 = 'close'

X_train_4 = data[X_features4]
y_train_4 = data[target_column4]

close_predictor_model = LinearRegression()
close_predictor_model.fit(X_train_4, y_train_4)

# Predicting the values for the next year
starting_date = '2022-02-01'
current_date = datetime.strptime(starting_date, '%Y-%m-%d')
end_date = datetime(current_date.year, 12, 31)

with open("datasets\open_predicted_values.csv", mode="w", newline="") as csv_file:

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['time', 'open', 'high', 'low', 'close','volume'])

    while (current_date <= end_date):

        high_predict = high_predictor_model.predict(np.array([open_value_start]).reshape(-1,1))[0]
        low_predict = low_predictor_model.predict(np.array([open_value_start,high_predict]).reshape(-1,2))[0]
        volume_predict = volume_predictor_model.predict(np.array([open_value_start,high_predict,low_predict]).reshape(-1,3))[0]
        close_predict = close_predictor_model.predict(np.array([open_value_start,high_predict,low_predict,volume_predict]).reshape(-1,4))[0]
        csv_writer.writerow([
            current_date.strftime('%Y-%m-%d'),
            open_value_start,
            high_predict,
            low_predict,
            close_predict,
            volume_predict

        ])

        open_value_start = close_predict
        current_date += timedelta(days=1)