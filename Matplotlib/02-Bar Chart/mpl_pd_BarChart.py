from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

data = pd.read_csv('data.csv')
IDs = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

lang_counter = Counter()
for response in lang_responses:
    lang_counter.update(response.split(';'))

languages = []
popularity = []

for item in lang_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.ylabel('Programming Languages')
plt.xlabel('Number of people who use')
plt.title('Most Popular Languages')
plt.legend()
plt.tight_layout()

plt.show()