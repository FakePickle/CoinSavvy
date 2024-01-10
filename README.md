# CoinSavvy Crypto Price Prediction Model

## Overview

Welcome to the CoinSavvy Crypto Price Prediction Model! This Python script utilizes a linear regression model to predict Bitcoin's closing prices based on historical data. The model considers the ```open``` and ```volume``` features to make predictions.

## How to Use

- Clone the repository.

    ```bash
    git clone https://github.com/FakePickle/CoinSavvy.git
    ```

- Install required dependencies

    ```bash
    pip install -r requirements.txt
    ```

- Run the model

    ```bash
    cd final_model
    python final_model.py
    ```

## Results:

The script will generate a CSV file (`final_predicted_values.csv`) containing the predicted and actual closing values. Additionally, it will display the Mean Squared Error on both the training and test sets.
\
A plot comparing the actual and predicted closing values will be displayed.

## Parameters

*   `ticker`: The cryptocurrency symbol (default is "BTC-USD").
*   `start_date`: Start date for historical data (default is "2018-02-01").
*   `end_date`: End date for historical data (default is "2022-01-01").

## File Structure
    ├── builder_models
    |    ├── dataset_builder.py
    |    ├── model_tester_btcusdt.ipynb
    |    ├── model_tester.ipynb
    |    ├── open_prediction_model.ipynb
    |    ├── open_prediction_model.py
    |    ├── ridge_test_model.ipynb
    ├── datasets
    |    ├── final_predicted_values.csv
    |    ├── open_predicted_values.csv
    |    ├── testing_dataset.csv
    |    ├── training_dataset.csv
    ├── final_model
    |    ├── final_predicted_values.py
    ├── requirements.txt
    ├── LICENSE
    ├── README.md

*   `final_model/final_predicted_values.py`: The main script for the Bitcoin price prediction model.
*   `datasets/`: Directory containing the generated CSV file with predicted values.

## Notes

*   The script uses historical data from Yahoo Finance (`yfinance`) for training and testing the model.
*   The linear regression model considers ```open``` and ```volume``` features for predictions.
*   Adjust the `start_date` and `end_date` variables in the script to fetch data for different time periods.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

[Harsh Mistry](https://github.com/FakePickle)
\
[Vikranth Udandarao](https://github.com/Vikranth3140)
\
[Noel Tiju](https://github.com/noeltiju)
\
[Mehul Agrawal](https://github.com/Mehul-Ag20)

Feel free to explore, experiment, and contribute to enhancing the model.

**Disclaimer**: Predictive models may not guarantee accurate results. Use with caution and consider additional factors for making financial decisions.

Thank you for exploring the Bitcoin Price Prediction Model! 🚀📈
\
Happy predicting!