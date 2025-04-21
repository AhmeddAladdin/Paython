# I can use (')
a = "I'm Ahmed"
b = 'I\'m Ahmed'
print(a),print(b)

# Another ways to connect
a = "Ahmed"
b = 13
print("I'm " + a + " my age " + str(b))
print("I'm %s my age %d" % (a, b))
'''
%s => string
%d => digits
%f => float
'''
print("I'm {:s} my age {:d}" .format (a, b))

# another way to print many lines
a = "I'm Ahmed\nMy age is 13"
b = """I'm Ahmed
My age is 13"""
print(a),print(b)

'''
-----------------------
----->Input users<-----
-----------------------
'''
input() # How to use this function?

# Example:
name = input("Enter your name: ")
m = input("Enter your middel name: ")
l = input("Enter your last name: ")
print("Hello %s %s %s I'm happy to see you." % (a, m, l))
# we notice here some problems, How to solve it??

# Method 1: .strip() ==> remove spaces that we don't need.
a = input("Enter your name: ")
m = input("Enter your middel name: ")
l = input("Enter your last name: ")
print("Hello %s %s %s I'm happy to see you." % (a.strip(), m.strip(), l.strip()))
# another problem is still here.

# Method 1, 2:
# .capitalize() ==> Make just the first char. capital
# .title() ==> Make the first char. capital for each word in the sentence
a = input("Enter your name: ")
m = input("Enter your middel name: ")
l = input("Enter your last name: ")
print("Hello %s %s %s I'm happy to see you." % (a.strip().title(), m.strip().title(), l.strip().title()))
# The line is too big!!

a = input("Enter your name: ")
m = input("Enter your middel name: ")
l = input("Enter your last name: ")

a = a.strip().title()
m = m.strip().title()
l = l.strip().title()

print("Hello %s %s %s I'm happy to see you." % (a, m, l))
# ========================================================