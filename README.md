# CoinSavvy BTC Price Prediction Model

As a part of our Hackathon. We have tried to explore different models which we could use to predict the closing price in the future.
\
We have compiled a predictive model for Bitcoin prices based on the historical data from 1st January, 2018 to 31st December, 2022.
\
We have worked our way through one approach in our modeling process but then had to shift to another approach as it was deviating a lot from the actual values.
\
We would like to take you through our journey in this GitHub page.

## Initial Model: First Day's Open Value

In our initial attempt, we developed a model focusing solely on the first day's ```open``` value of Bitcoin. 
\
This approach aimed to gauge the predictive power of this single feature in forecasting future prices by trying to predict the ```high``` value solely based on ```open``` value,
\
and then predict the ```low``` value based on ```open``` and ```high```,
\
and then predct the ```volume``` value based on ```open```, ```high``` and ```low``` values,
\
and then finally predicting the ```close``` for the day, which will be the ```open``` value for the next day.

But the predictions given by the model was not accurate and deviated a lot from the testing dataset.

## Enhanced Model: First Day's Open and Volume Value

So, we enhanced our approach by incorporating two features: the ```open``` price and the ```volume``` traded on the respective day.
\
This more comprehensive model aimed to capture additional market dynamics.

We then got the predcted values closer to the actual dataset and devated a lot lesser than the actual dataset.