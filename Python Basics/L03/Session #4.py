'''
======================================
-----> for loop inside for loop <-----
======================================
'''

person = ['Ahmed', 'Osama', 'ALi', 'Khaled']
skills = ['programming', 'network', 'creativity']

for name in person:  # outer for
    print(f'ENG: {name} skills is:')
    for skill in skills:  # inner for
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

# =======================================
print('=' * 40)
# =======================================

'''
======================================
-----> Advanced dictionary loop <-----
======================================
'''

lang = {
    "python": '90%',
    'css': '80%',
    'html': '85%'
}
# print(lang.items())

for skill in lang:  # method_1
    print(f'{skill} = {lang[skill]}')

for skillName, skillProgress in lang.items():    # method_2
    print(f'{skillName} = {skillProgress}')

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

for name, skills in engineers.items():
    print(f'Skills and progress for "{name}" is:')
    for skillName, progress in skills.items():
        print(f' -{skillName} = {progress}')

# =======================================
print('=' * 40)
# =======================================

mySkills = {
    'networking': {
        'progress': '70%',
        'time': '1 month'
    },
    'python': {
        'progress': '80%',
        'time': '4 month'
    },
    'electronics': {
        'progress': '82%',
        'time': '1 year'
    }
}

for skillName, skillINFO in mySkills.items():
    print(f'my progress in {skillName} is:')
    for info, value in skillINFO.items():
        print(f' -{info} = {value}')