"""
===================
-----> Lists <-----
===================
"""

# 1- list items are enclosed in []
mylist = ['Ahmed', 'Ali', 'Amer', 'Khaled']
print(mylist)

# 2- list can have different data types
mylist = ['Ahmed', 'Ali', 'Amer', 1, 83.4, True]
print(mylist)

# 3- it's ordered, use index to access item
mylist = ['Ahmed', 'Ali', 'Amer', 1, 83.4, True]
print(mylist[2])
print(mylist[-1])
print(mylist[1:5:1])

# 4- list item is not unique
mylist0 = ['one', 'two', 'one', 'one']


# 5- lists are mutable => Replace, Delete, Edit
# replace:
mylist = ['Ahmed', 'Ali', 'Amer', 1, 83.4, True]
mylist[2] = "lion"
print(mylist)

# Delete:
mylist = ['Ahmed', 'Ali', 'Amer', 1, 83.4, True]
mylist[2:3] = []
print(mylist)

# Edit: delete then add
mylist = ['Ahmed', 'Ali', 'Amer', 1, 83.4, True]
mylist[2:3] = ["a", 'c', 'dd']
print(mylist)

# =================================================

"""
===========================
-----> Lists Methods <-----
===========================
"""

# .append() : add item at the end
friends = ['Mahmoud', 'Ali', 'Osama']
oldfriends = ['Ahmed', 'mariam', 'Mona']

friends.append("Amr")
print(friends)
print(friends[3])

oldfriends.append("khaled")
print(oldfriends)
print(oldfriends[3])

friends.append(oldfriends)
print(friends)
print(friends[4])
print(friends[4][2])

# .extend() : make them one
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
a.extend(b)
print(a)

# .remove()
z = [1, 2, 2, 3, 4, 'a', 'b', 'c', 'd']
z.remove(2)
print(z)

# .sort() : ترتيب من الصغير الى الكبير
num = [21, 543, 2, -10, -51, 234.5, 234, -55.5]
num.sort()
print(num)
# .sort() = .sort(reverse=False) : ترتيب من الصغير الى الكبير
num.sort(reverse=False)
print(num)
# .sort(reverse=True) : ترتيب من الكبير الى الصغير
num.sort(reverse=True)
print(num)

# .reverse()
var = [21, 4.45, 'Ali', 0.84, True]
var.reverse()
print(var)

# .clear()
listtt = ['Ahmed', 'mariam', 'Mona', 'khaled']
listtt.clear()
print(listtt)

# .copy()
listtt = ['Ahmed', 'mariam', 'Mona', 'khaled']
qq = listtt.copy()
print(listtt)
print(qq)

# .count()
asd = [1, 33, 1, 1, 23, 1]
print(asd.count(1))

# . index()
listtt = ['Ahmed', 'mariam', 'Mona', 'khaled']
print(listtt.index('Mona'))

# .insert( , )
listtt = ['Ahmed', 'mariam', 'Mona', 'khaled']
listtt.insert(1, "Key")
print(listtt)
listtt.insert(-1, "Key")
print(listtt)