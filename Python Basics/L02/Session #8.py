'''
===================
-----> Tuple <-----
===================
'''

# [1] Items are enclosed in ()
mytuple = ('Ahmed', 21, True)
print(mytuple)
print(type(mytuple))

# [2] can remove () if you want
mytuple = 'Ahmed', 21, True
print(mytuple)
print(type(mytuple))

# [3] tuple are ordered, can use index
mytuple = ('Ahmed', 21, True)
print(mytuple[1])

# [4] can't be edited

# [5] items aren't unique
a = (1, 2, 'one', True, 1, "one")
print(a)

# [6] can have any type of data
a = (1, 2, 'one', True, 1, "one")
print(a)

# =========================================

# Tuple with one item ?
A = ("Ahmed")
a = "Ahmed"
print(type(A))
print(type(a))

# so if you want to put one item put ',' at the end
A = ("Ahmed",)
a = "Ahmed",
print(type(A))
print(type(a))

# =========================================

# tuple concatenation
a = 1, 2, 3, 4
b = 5, 6, 7, 8
c = a + b
print(c)

# tuple, list, string: repeat = (*)
mytuple = ('a', 'b', 'c')
mylist = [1, 2, 3]
mystr = "Ahmed"
print(mystr * 5)
print(mylist * 5)
print(mytuple * 5)

# =========================================

'''
===========================
-----> Tuple Methods <-----
===========================
'''

# .count()
a = (1, 2, 3, 2, 4, 5, 2, 6, 7, 8, 2)
print(a.count(2))

# .index()
b = (13, 15, 14, 21, 19, 17, 20)
print(b.index(14))

# ====================================

# tuple destruct
q = ('A', 'B', 'C')
x, y, z = q
print(x)
print(y)
print(z)

q = ('A', 'B', 4, 'C')
x, y, _, z = q
print(x)
print(y)
print(z)
