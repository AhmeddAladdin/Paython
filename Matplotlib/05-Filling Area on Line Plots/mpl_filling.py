import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('data1.csv')
ages = data1['Age']
dev_salary = data1['All_Devs']
py_salary = data1['Python']
js_salary = data1['JavaScript']
overall_median = data1["All_Devs"].median()

plt.plot(ages, dev_salary, color= '#F80101',
	linestyle= '--', label= 'All Devs')
plt.plot(ages, py_salary, color= '#6EE91B',label= 'Python')

plt.fill_between(ages, py_salary, overall_median, alpha= 0.25, 
	where= (py_salary>overall_median), interpolate= True, label= 'Above Median')

plt.fill_between(ages, py_salary, overall_median, alpha= 0.25, 
	where= (py_salary<=overall_median), interpolate= True, color= 'red', label= 'Below Median')

#plt.fill_between(ages, py_salary, dev_salary, alpha= 0.25, 
#	where= (py_salary>dev_salary), interpolate= True, label= 'Above Avg')

#plt.fill_between(ages, py_salary, dev_salary, alpha= 0.25, 
#	where= (py_salary<=dev_salary), interpolate= True, color= 'red', label= 'Below Avg')

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.legend()

plt.show()