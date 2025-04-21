# index
a = 'Ahmed'
print(a[2]) # start from zero
print(a[-2])

# Slicing
b = 'My name is Ahmed'
# print(var[start:end])
# print(var[start:end:step])
print(b[0:5]) # end not included
print(b[:5]) # if you didn't write start it will start from zero
print(b[0:]) # if you didn't write end it will be end at the end
print(b[2:5:1])

# len() give you number of items in your variable
c = 'My name is Ahmed'
print(len(c))

# =======================

'''
===================
----> methods <----
===================
'''

# method 1 : strip() , rstrip() , lstrip()
# the sign you write in () it will be removed
x = '    My name is Ahmed    '
print(x.strip())
print(x.rstrip())
print(x.lstrip())
y = '####My name is Ahmed####'
print(x.strip('#'))
r = '#@#@My name is Ahmed#@#@'
print(r.strip('#@'))

# method 2 : title()

# method 3 : capitalize()

# method 4 : upper()
l = 'ahmed'
print(l.upper())

# method 5 : lower()
k = 'ahmed'
print(k.lower())

# method 6 : zfill()
q, w, e = '1', '12', '432'
print(q.zfill(3))
print(w.zfill(3))
print(e.zfill(3))

# method 7 : split() rsplit()
f = "my name is ahmed"
print(f.split())
f = "my-name-is-ahmed"
print(f.split('-'))
f = "my name is ahmed"
print(f.split(" ", 1))

f = "my name is ahmed"
print(f.rsplit(" ", 1))

# method 8 : center(num, "sign")
s = 'ahmed'
print(s.center(10))
print(s.center(10, '$'))

# method 9 : count("the item", start, end)

z = 'my name is ahmed and my grandfather name is ahmed also'
print(z.count('ahmed'))
print(z.count('ahmed', 5, 12))

# method 10 : swapcase()
d = 'my name is ahmed'
v = 'MY NAME IS AHMED'
print(d.swapcase())
print(v.swapcase())

# method 11 : startswith()
i = 'i am ahmed'
print(i.startswith('i'))
print(i.startswith('i',0,5))

# method 12 : endswith()

i = 'i am ahmed'
print(i.endswith('d'))
print(i.endswith('i',3,9))

# method 13 : index()
p = 'my name is ahmed'
print(p.index('n'))
print(p.index('n',2,8))
print(p.index('n',5,8))

# method 14 : find()
p = 'my name is ahmed'
print(p.find('n'))
print(p.find('n',2,8))
print(p.find('n',5,8))

# method 15 : rjust() ljust()
j = 'ahmed'
print(j.rjust(10)),print(j.ljust(10))
print(j.rjust(10, '#')),print(j.ljust(10, '#'))
