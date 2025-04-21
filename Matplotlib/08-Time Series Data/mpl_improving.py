import matplotlib.pyplot as plt
import pandas as pd

data5 = pd.read_csv('data5.csv')

data5['Date'] = pd.to_datetime(data5['Date']) # Convert the date column to datetime
data5.sort_values('Date', inplace=True) # Sort the data by date
price_date = data5['Date']
price_close = data5['Close']

plt.style.use('seaborn-v0_8')
plt.plot_date(price_date, price_close)

plt.plot_date(price_date, price_close, linestyle='solid') # to add a solid line to the plot

# to change the format of the date on the x axis automatically
plt.gcf().autofmt_xdate()

# to change the format of the date on the x axis automatically
plt.gcf().autofmt_xdate()  # gcf() returns the current figure

# adding dateformatter to change the format of the date on the x axis
from matplotlib.dates import DateFormatter
date_format = DateFormatter('%b, %d %Y') 

# plt.gca() returns the current axes
plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('final look.png')
plt.show()