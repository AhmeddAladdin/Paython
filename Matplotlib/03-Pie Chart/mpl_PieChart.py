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

slices = popularity[:5]
labels = languages[:5]
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels= labels, explode= explode, shadow= True,
        startangle= 90, autopct= '%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.tight_layout()

plt.show()