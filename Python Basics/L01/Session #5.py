z = input("Enter any thing: ")
print(type(z)) # str
# convert it to integer and float also.
# ===================================

'''
1- == ?
2- != ?
'''
z, y = 10, "Ali"
print(z == 10), print(z != 9), print(y == "Ali")
# ===================================

'''
------------------------
----->if statement<-----
------------------------
'''

name = 'Ahmed'
country = 'Egypt'
course = 'python course'
price = 100
discount = 30

print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - discount))
# ==========================================

# but I want different discount for each country.

name = 'Ahmed'
country = 'Egypt'
course = 'python course'
price = 100

if country == "Egypt":
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 80))

elif country == "KSA":
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 70))

else:
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 30))
# ==========================================

# but what if I want different discount for every two or three country or more than this?
# ------------------------->(use logic operators: 'and' 'or' 'not')<-------------------------

name = 'Ahmed'
country = 'Egypt'
course = 'python course'
price = 100

if country == "Egypt" or country == 'KSA' :
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 80))

elif country == "Kuwait" or country == 'Emirates':
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 60))

else:
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 30))

