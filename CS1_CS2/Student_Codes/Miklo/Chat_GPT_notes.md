# measuring Pepsi stock price correlation to price to earnings ratio

This is a project we are going to just try.

## Chat General Pre-trained Transform prompt:
write python code to measure correlation between previous 12 month average price to earnings ratio and daily average stock price for Pepsi from 1990 to 2020

## Front note from Chat GPT

To measure the correlation between the previous 12 month average price to earnings ratio and daily average stock price for Pepsi from 1990 to 2020, we will need to do the following steps:

Retrieve historical price and earnings data for Pepsi from a reliable source (such as Yahoo Finance or Alpha Vantage).
Calculate the 12-month moving average for the price to earnings ratio.
Calculate the daily average stock price.
Merge the two data sets by date.
Calculate the correlation between the two data sets using a suitable statistical method (such as the Pearson correlation coefficient).

Here is an example Python code to perform these steps:
### Code is saved in Measuring_Correlations_between_ratios_and_stock_prices.py

## after note from Chat GPT
Note: In this example code, we have used the pandas_datareader library to retrieve the historical price and earnings data for Pepsi from Yahoo Finance. We have also used the yfinance library to override the default pandas_datareader data source, which has been known to have issues with retrieving data from Yahoo Finance. If you encounter any issues with data retrieval, you may need to check the documentation for these libraries to ensure that they are up-to-date and compatible with your version of Python.