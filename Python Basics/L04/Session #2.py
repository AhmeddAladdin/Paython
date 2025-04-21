"""
=====================================
-----> Packing & unpacking & * <-----
=====================================
"""

# *
print(1, 2, 3, 4)
mylist = [1, 2, 3, 4]
print(mylist)
print(*mylist)

# =====================================
print('=' * 40)
# =====================================


def say_hello(n1, n2, n3, n4):

    peoples = [n1 , n2, n3, n4]

    for name in peoples:

        print(f'Hello {name}')


say_hello('Ahmed', 'Omar', 'Yousef', 'Ali')

say_hello('Ahmed', 'Omar', 'Yousef', 'Ali', 'Khaled')

# =====================================
print('=' * 40)
# =====================================


def say_hello(*peoples):

    for name in peoples:

        print(f'Hello {name}')


say_hello('Ahmed', 'Omar', 'Yousef', 'Ali')

say_hello('Ahmed', 'Omar', 'Yousef', 'Ali', 'Khaled')

# =====================================
print('=' * 40)
# =====================================


def family(name, *kids):

    print(f'Hello {name}, your kids name is: ')

    for kid in kids:

        print(kid)


family('Ali', 'Malak', 'Aya', 'Amr')

# =====================================
print('=' * 40)
# =====================================

# **

def Myskills(**skills):

    for skill, progress in skills.items():

        print(f'your skill:{skill} => {progress}')


Myskills(python='60%', network='20%', robotics='40%')
