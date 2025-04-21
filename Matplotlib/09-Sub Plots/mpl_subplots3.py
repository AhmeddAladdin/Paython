import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('data1.csv')

ages = data1['Age']
dev_salaries = data1['All_Devs']
py_salaries = data1['Python']
js_salaries = data1['JavaScript']

# Now let's make each plot in a different fig.
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, label='All Devs', linestyle='--')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_xlabel('Ages', fontsize=12)
ax1.set_ylabel('Median Salary (USD)', fontsize=12)
ax1.set_title('Median Salary (USD) by Age', fontsize=12)

ax2.legend()
ax2.set_xlabel('Ages', fontsize=12)
ax2.set_ylabel('Median Salary (USD)', fontsize=12)
ax2.set_title('Median Salary (USD) by Age', fontsize=12)

plt.tight_layout()
fig1.savefig('final1.png')
fig2.savefig('final2.png')
plt.show()