"""
============================
-----> Function scope <-----
============================
"""

# training

myProgress = {
    'python': '50%',
    'network': '30%',
    'robotics': '70%'
}

mySkills = ['python', 'Network', 'robotics']


def showSkills(name, *skills, **skillsProgress):
    print(f'Hello {name}\nYour skills without progress:')

    for skill in skills:
        print(f'-{skill}')

    print('Your skills with progress:')

    for a, b in skillsProgress.items():
        print(f'-{a} => {b}')


showSkills('Ahmed', *mySkills, **myProgress)

# Scope:

# Global Scope & Local Scope

a = 4


def one():
    global a

    a = 1

    print(f'The number is {a}')


def two():
    a = 2

    print(f'The number is {a}')


print(f'The number is {a}')
one()
print(f'The number is {a}')
two()
