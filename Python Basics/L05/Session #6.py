"""
=================================
----> Iterable vs. Iterator <----
=================================
1- Iterable:
a) Object contain Data that can be iterated upon
b) Examples: string, list, set, tuple, dictionary.
-------------------------------------------------------
2- Iterator:
a) Used to iterate over iterable using next() method return 1 element at a time
b) You can generate iterator from iterable using iter() method
c) For loop already calls iter() on the iterable behind the scene
d) Gives "StopIteration" if there is no element
--------------------------------------------------------
"""
name = iter("Ahmed")


print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))


'''
for i in name:
    print(i)
'''