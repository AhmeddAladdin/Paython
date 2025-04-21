"""
===========================
-------> Functions <-------
===========================
[1] A function is a reusable block of code do a task
[2] Run when you call it
[3] Accept element to deal with, called (parameters)
[4] can do a task without returning data
[5] can do a task with returning data
========================================================
"""


# how to build a function…?

def say_hi():
    print('hello user, welcome to my function')


say_hi()

# ================================================
print("=" * 40)
# ================================================

# return :
'''
you can use it as you want, like: print it,
or put it in variable, or anything you want
return is the last line in function so the code will not read any line after it
'''
def data():
    return "My name is Ali, I am 45 years old"


print(data())
myData = data()
print(myData)

# ================================================
print("=" * 40)
# ================================================

'''
============================
-------> Parameters <-------
============================
'''

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


fullData('ahmed   ', '12',     'MANsouRA')