"""
============================
-------> Parameters <-------
============================
"""

# if I want welcome some peoples (old way)
a, b, c = 'Ahmed', 'ALi', 'Osama'
print(f'Hello {a}')
print(f'Hello {b}')
print(f'Hello {c}')

# ================================================
print("=" * 40)


# ================================================

# if I want welcome some peoples (with function)


def say_hello(name):
    print(f'Hello {name}')


say_hello("Ahmed")
Name = 'Ali'
say_hello(Name)


# another example:


def addition(n1, n2):
    print(n1 + n2)


addition(123, 321)

# ================================================
print("=" * 40)


# ================================================

# more advanced using if statement:


def addition(n1, n2):
    if type(n1) == str or type(n2) == str:
        print("ONLY data type int or float allowed")
    else:
        print(float(n1) + float(n2))


addition('123', 321)
addition(123, 'Ali')
addition(123, 321)


# another example:


def fullData(name, age, address):
    print(
        f'Hello {name.strip().capitalize()},'
        f' your age is {int(age)},'
        f' and you live in {address.strip().capitalize()}')


fullData('ahmed   ', '12', 'MANsouRA')

# ================================================
print("=" * 40)


# ================================================

# default parameter

def fullData(name='UnKnown', age='UnKnown', address='UnKnown'):
    print(
        f'Hello {name.strip().capitalize()},'
        f' your age is {age},'
        f' and you live in {address.strip().capitalize()}')


fullData('ahmed   ', '12', 'MANsouRA')
fullData('ali   ', '22')
fullData('ramy   ')
fullData()

# ================================================
print("=" * 40)
# ================================================


