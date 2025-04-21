import matplotlib.pyplot as plt
import pandas as pd

data5 = pd.read_csv('data5.csv')

data5['Date'] = pd.to_datetime(data5['Date']) # Convert the date column to datetime
data5.sort_values('Date', inplace=True) # Sort the data by date
price_date = data5['Date']
price_close = data5['Close']

plt.style.use('seaborn-v0_8')
plt.plot_date(price_date, price_close)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
#plt.savefig('still dots.png')
plt.show()
