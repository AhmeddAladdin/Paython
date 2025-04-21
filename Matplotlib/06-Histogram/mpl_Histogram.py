import matplotlib.pyplot as plt
import pandas as pd

data3 = pd.read_csv('data3.csv')
IDs = data3['Responder_id']
ages = data3["Age"]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
median_age = ages.median()
color = '#FC0505'

plt.style.use('fivethirtyeight')

plt.hist(ages, bins= bins, edgecolor= 'black', log= True)
plt.axvline(median_age, color= color, label= 'Median Age')

plt.title("Ages for Respondents")
plt.xlabel('Ages')
plt.ylabel('Total Respodents')
plt.legend()

#plt.savefig('Hist with median.png')
plt.show()