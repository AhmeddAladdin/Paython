'''
========================
-----> Dictionary <-----
========================
'''

'''
[1] Dict. items are enclosed in curly bracts {}
[2] Dict. items are contain key : value
[3] Dict. key need to be an immutable ->(strings, numbers, tuple), list not allowed
[4] Dict. value can be any type of data
[5] Dict. key need to be unique
[6] Dict. isn't ordered, can access its element with key
'''

user = {
    'name': 'Ali',
    'age': 30,
    'country': 'Egypt',
    'skills': ['programming', 'network', 'robotics'],
    'height': 176.5
}
print(user)

# to access any element:
print(user['age'])
print(user.get('age'))

print(user.keys())  # to get all keys
print(user.values())  # to get all values

# Two_dimensional Dict.
subjects = {
    'one': {
        'name': 'Arabic',
        'progress': '83%'
    },
    'two': {
        'name': 'Math',
        'progress': '90%'
    },
    'three': {
        'name': 'science',
        'progress': '85%'
    }
}
# Dict. access
print(subjects)
print(subjects['one'])
print(subjects['three']['name'])
# Dict. length
print(len(subjects))
print(len(subjects['two']))

# many dicts. in one

person1 = {
    'name': 'Ahmed',
    'age': 21
}

person2 = {
    'name': 'Ali',
    'age': 24
}

person3 = {
    'name': 'Hany',
    'age': 19
}

all_dicts = {
    'one': person1,
    'two': person2,
    'Three': person3
}
print(all_dicts)

'''
===================
----> Methods <----
===================
'''

# .clear()

# .update() : add new item
member = {
    'name': "Khaled"
}
member['age'] = 33
print(member)
member.update({'country': 'Egypt'})
print(member)

# .copy()

# .keys(), .values()

# .setdefault()
member = {
    'name': "Khaled"
}
print(member)
print(member.setdefault('name', 'Ahmed'))
print(member)
print(member.setdefault('age', 13))
print(member)

# .popitem()
member = {
    'name': "Khaled"
}
member.update({'country': 'Egypt'})
print(member.popitem())

# .items()
data = {
    'name': 'Ahmed',
    'country': 'KSA'
}
all_items = data.items()
data['age'] = 29
print(all_items)

# .fromkeys()
a = 'name', 'age', 'hoppy'
b = 'Ahmed', 21, 'football'

print(dict.fromkeys(a, b))