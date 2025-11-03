import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

# Set the start and end dates for the data retrieval
start_date = '1990-01-01'
end_date = '2020-12-31'

# Retrieve historical price and earnings data for Pepsi using Yahoo Finance
yf.pdr_override()
pep = pdr.get_data_yahoo("PEP", start=start_date, end=end_date)

print(pep.head())
print(pep.tail())

# Calculate the 12-month moving average for the price to earnings ratio
pep['PEMA12'] = pep['Close'].rolling(window=252).mean() / pep['Earnings'].rolling(window=252).mean()

# Calculate the daily average stock price
pep['PriceMA'] = pep['Close'].rolling(window=1).mean()

# Merge the two data sets by date
pep_corr = pd.merge(pep[['PEMA12', 'PriceMA']], pep[['PEMA12', 'PriceMA']], left_index=True, right_index=True, suffixes=('_earnings', '_price'))

# Calculate the correlation between the two data sets
corr = np.corrcoef(pep_corr['PEMA12_earnings'], pep_corr['PriceMA_price'])[0, 1]

print("Correlation between previous 12-month average price to earnings ratio and daily average stock price for Pepsi from 1990 to 2020:", corr)
