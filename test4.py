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

# Daily returns
daily_pct_change = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_change`
print(daily_pct_change)

# FORMULA OF DAILY PCT CHANGE
#r1 = (pt/ p(t-1)) - 1

daily_pct_change.hist(bins=50)
plt.show()

# Pull up summary statistics
print(daily_pct_change.describe())

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()

# Print `cum_daily_return`
print(cum_daily_return)
plt.show(cum_daily_return)
# Resample the cumulative daily return to cumulative monthly return 
cum_monthly_return = cum_daily_return.resample("M").mean()

# Print the `cum_monthly_return`
print(cum_monthly_return)