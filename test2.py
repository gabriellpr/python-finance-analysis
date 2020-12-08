import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt

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

# Show the plot
plt.show()