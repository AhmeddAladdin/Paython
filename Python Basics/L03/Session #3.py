'''
======================
-----> for loop <-----
======================
'''

mylist = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

for numbers in mylist:
    print(numbers)
else:
    print('loop is finished')

# =======================================
print('=' * 40)
# =======================================

list1 = [13, 22, 21, 17, 14, 16, 20, 15]

for num in list1:
    if num % 2 == 0:
        print("the number = {:d} is even".format(num))
    else:
        print("the number = {:d} is odd".format(num))
else:
    print('the numbers is finished')

# =======================================
print('=' * 40)
# =======================================

name = input('Enter your first name:')
for letter in name:
    print(letter.upper())
else:
    print('the letters is finished')

# =======================================
print('=' * 40)
# =======================================

# range()
Range = range(1, 100)
for numbers in Range:
    print(numbers)

# =======================================
print('=' * 40)
# =======================================

subjects = {
    'Arabic': '90%',
    'English': '85%',
    'Frensh': '80%',
    'Math': '95%',
    'Mechanics': '89%',
    'Statics': '81%'
}
# print(subjects[Arabic])
# print(subjects.get(Arabic))
for sub in subjects:
    # print(sub)
    print('My rank in {:s} = {:s}'.format(sub, subjects[sub]))

# =======================================
print('=' * 40)
# =======================================

'''
======================================
-----> for loop inside for loop <-----
======================================
'''

person = ['Ahmed', 'Osama', 'ALi', 'Khaled']
skills = ['programming', 'network', 'creativity']

for name in person:
    print(f'ENG: {name} skills is:')
    for skill in skills:
        print(f' -{skill}')

# =======================================
print('=' * 40)
# =======================================

engineers = {
    'Ahmed': {
        'programming': '80%',
        'network': '65%',
        'creativity': '99%'
    },
    'Osama': {
        'programming': '98%',
        'network': '50%',
        'creativity': '90%'
    },
    'ALi': {
        'programming': '88%',
        'network': '60%',
        'creativity': '95%'
    },
    'Khaled': {
        'programming': '70%',
        'network': '99%',
        'creativity': '82%'
    }
}

# print(engineers['Osama'])
# print(engineers['Ali']['network'])

for name in engineers:
    print(f'Skills and progress for "{name}" is:')
    for skill in engineers[name]:
        print(f' -{skill} = {engineers[name][skill]}')