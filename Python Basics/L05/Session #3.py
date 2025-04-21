"""
================================
-----> Built in functions <-----
================================
"""

# map()

products = [
    ('mouse', 250),
    ('keyboard', 350),
    ('screen', 650),
    ('laptop', 80000)
]
# method 1
prices1 = []
for item1 in products:
    prices1.append(item1[1])

print(prices1)

# method 2
prices2 = list(map(lambda item2: item2[1], products))
print(prices2)


# method 3
def items(item3):
    return item3[1]

# ==========================================

# filter()
Degrees = [
    ('Ahmed', 98),
    ('Ibrahim', 66),
    ('Osama', 36),
    ('Ali', 51),
    ('Amr', 49),
    ('Saad', 74)
]

successful = list(filter(lambda a : a[1] > 50, Degrees))
print(successful)

# another Example
names = ['Ahmed', 'Osama', 'Ali', 'Othman', 'Khaled', 'Amr']
mylist = list(filter(lambda name: name.startswith('A'), names))
print(mylist)
# ===========================================

# reduse()
from functools import reduce
num = [4, 5, 10, 11]


def summ(n1, n2):
    return n1 + n2


print(reduce(summ, num))
# or
print(reduce(lambda n1, n2:n1*n2, num))