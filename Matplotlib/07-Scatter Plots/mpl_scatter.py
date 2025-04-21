import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data4 = pd.read_csv('2019-05-31-data.csv')
view_count = data4['view_count']
likes = data4['likes']
ratio = data4['ratio']

plt.style.use('seaborn-v0_8')
plt.figure(figsize=(12, 6))
plt.scatter(view_count, likes, c= ratio, cmap= 'cool'
	, edgecolor= 'black',linewidth=1, alpha= 0.75 )

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.title('Trending Youtube Videos')
plt.tight_layout()

#plt.savefig('Hist with median.png')
plt.show()