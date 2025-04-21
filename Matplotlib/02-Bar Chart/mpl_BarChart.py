from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lang_counter = Counter()
    for row in csv_reader:
        lang_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in lang_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse

plt.barh(languages, popularity)
plt.ylabel('Programming Languages')
plt.xlabel('Number of people who use')
plt.title('Most Popular Languages')
plt.legend()
plt.tight_layout()

plt.show()