import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

minute = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']

plt.stackplot(minute, player1, player2, player3, labels= labels)

plt.title('First Stack Plot')
plt.tight_layout()
plt.legend()
plt.show()