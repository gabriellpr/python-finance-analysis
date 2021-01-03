import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import numpy as np

#Day percent change

aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2006, 10, 1),
                                  end=datetime.datetime(2012, 1, 1))

aapl.to_csv('appl.csv')                                  
df = pd.read_csv('appl.csv', header=0, index_col='Date', parse_dates=True)                                  

# Add a column `diff` to `aapl` 
aapl['diff'] = aapl.Open - aapl.Close

# Delete the new `diff` column
#del aapl['diff']
#print(aapl)
aapl['Close'].plot(grid=True)

# Assign `Adj Close` to `daily_close`
daily_close = aapl[['Adj Close']]

# Daily returns
daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Inspect daily returns
print(daily_pct_change)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
print(daily_log_returns)

# Show the plot
#plt.show()

# Resample `aapl` to business months, take last observation as value 
monthly = aapl.resample('BM').apply(lambda x: x[-1])

# Calculate the monthly percentage change
monthly.pct_change()

# Resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()

# Calculate the quarterly percentage change
print(quarter.pct_change())

# Daily returns
daily_pct_change = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_change`
print(daily_pct_change)