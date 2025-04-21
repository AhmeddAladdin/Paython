"""
===================
-----> sets <-----
===================
"""

# 1- set items are enclosed in {}
myset = {'Ahmed', 'Ali', 'Amer', 'Khaled'}
print(myset)

# 2- set is not ordered or indexed
myset = {'Ahmed', 'Ali', 'Amer', 'Khaled'}
print(myset)
print(myset[2])

# 3- indexing and slicing can not be done


# 4- can only contain immutable data types, can't contain lists
mysett = {"ahmed", 1002, True, 12.2}

# 5- set items are unique

# =================================================

"""
===========================
-----> Sets Methods <-----
===========================
"""

# .clear()

# .union()
a = {1, 2, 3}
b = {"one", 'two', 'three'}
print(a | b)
print(a.union(b))

# .add()
q = {1, 2, 3}
q.add(4)
print(q)

# .copy()

# .remove()
q = {1, 2, 3}
q.remove(1)
print(q)
q.remove(9)
print(q) #??

# .discard()
q = {1, 2, 3}
q.discard(1)
print(q)
q.discard(9)
print(q) #??

# .update()
a = {1, 2}
b = {2, "one", 'two', 1}
a.update(b)
print(a)

# ==========================================

# .difference()
w = {1, 2, 3, 4}
e = {1, 2, 'one'}
print(w)
print(w.difference(e))
print(w)

# .difference_update()
w = {1, 2, 3, 4}
e = {1, 2, 'one'}
print(w)
w.difference_update(e)
print(w)

# .intersection()
w = {1, 2, 3, 4}
e = {1, 2, 'one'}
print(w)
print(w.intersection(e))
print(w)

# .intersection_update()
w = {1, 2, 3, 4}
e = {1, 2, 'one'}
print(w)
print(w.intersection_update(e))
print(w)

# .symmetric_difference()
w = {1, 2, 3, 4}
e = {1, 2, 'one'}
print(w)
print(w.symmetric_difference(e))
print(w)

# .symmetric_difference_update()
w = {1, 2, 3, 4}
e = {1, 2, 'one'}
print(w)
print(w.symmetric_difference_update(e))
print(w)

# ==========================================

# .issuperset()
r = {1, 2, 3, 4}
p = {1, 2, 3}
o = {1, 2, 3, 4, 5}
print(r.issuperset(p))  # print(p.issubset(r))
print(r.issuperset(o))

# .issubset()
r = {1, 2, 3, 4}
p = {1, 2, 3}
o = {1, 2, 3, 4, 5}
print(r.issubset(p))
print(r.issubset(o))

# .isdisjoint()
A = {1, 2, 3, 4}
B = {1, 2, 3}
C = {11, 12, 13}
print(A.isdisjoint(B))
print(A.isdisjoint(C))