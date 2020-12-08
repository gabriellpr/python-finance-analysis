import pandas as pd
import pandas_datareader as pdr
import datetime

aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2006, 10, 1),
                                  end=datetime.datetime(2012, 1, 1))

aapl.to_csv('appl.csv')                                  
df = pd.read_csv('appl.csv', header=0, index_col='Date', parse_dates=True)                                  

# Inspect the index 
aapl.index

# Inspect the columns
aapl.columns

# Select only the last 10 observations of `Close`
ts = aapl['Close'][-10:]

# Check the type of `ts` 
type(ts)

# Inspect the first rows of November-December 2006
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())

# Inspect the first rows of 2007 
print(aapl.loc['2007'].head())

# Inspect November 2006
print(aapl.iloc[22:43])

# Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01
print(aapl.iloc[[22,43], [0, 3]])

# TO KNOW BETTER MY DATA
# Sample 20 rows
sample = aapl.sample(20)

# Print `sample`
print(sample)

# Resample to monthly level 
monthly_aapl = aapl.resample('M').mean()

# Print `monthly_aapl`
print(monthly_aapl)