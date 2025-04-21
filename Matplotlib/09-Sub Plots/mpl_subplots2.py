import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('data1.csv')

ages = data1['Age']
dev_salaries = data1['All_Devs']
py_salaries = data1['Python']
js_salaries = data1['JavaScript']

fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, # Sharing the x axis between the two plots
                       sharey=True) # Sharing the y axis between the two plots
ax[0].plot(ages, dev_salaries, label='All Devs', linestyle='--')
ax[1].plot(ages, py_salaries, label='Python')
ax[1].plot(ages, js_salaries, label='JavaScript')

ax[0].legend()
ax[0].set_ylabel('Median Salary (USD)', fontsize=12)
ax[0].set_title('Median Salary (USD) by Age', fontsize=12)

ax[1].legend()
ax[1].set_xlabel('Ages', fontsize=12)
ax[1].set_ylabel('Median Salary (USD)', fontsize=12)

plt.tight_layout()
#plt.savefig('second.png')
plt.show()