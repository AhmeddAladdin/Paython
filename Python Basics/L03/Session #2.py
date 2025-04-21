'''
==================
-----> QUIZ <-----
==================
'''

'''
q1.
Find the output of the following program: 

nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
print (nameList[1][-1])

a) r
b) b
c) D
d) k

======================================================
q2.
Find the output of the following program: 

geekCodes = [1, 2, 3, 4] 
geekCodes.append([5,6,7,8]) 
print(geekCodes) 

1. [1,2,3,4,5,6,7,8]
2. [1,2,3,4]
3. [1,2,3,4,[5,6,7,8]]
4. [1,2,3,4][5,6,7,8]

======================================================
q3.
Find the output of the following program: 

# statement 1
list1 = range(100, 110) 
# statement 2
print (list1.index(105))

1. 105
2. 5
3. 106
4. 104

======================================================
q4.
Find the output of the following program: 

list1 = [1, 2, 3, 4, 5, 0] 
list2 = list1 
list2[0] = 0; 
print( list1)  

1. [1, 2, 3, 4, 5, 0]
2. [0,1, 2, 3, 4, 5]
3. [0, 2, 3, 4, 5]
4. [1, 2, 3, 4, 0]

======================================================
q5.
Find the output of the following program: 

list1 = [1998, 2002] 
list2 = [2014, 2016] 
print ((list1 + list2)*2)

1. [1998, 2002, 2014, 2016, 1998, 2002, 2014, 2016]
2. [1998, 2002, 2014, 2016]
3. [1998, 2002, 1998, 2002]
4. [2014, 2016, 2014, 2016]

======================================================
q6.
Find the output of the following program: 

list1 = ['physics', 'chemistry', 1997, 2000] 
print (list1[1][-1])

1. p
2. y
3. 7
4. 2

======================================================
q7.
Find the output of the following program: 

list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for', 'Geeks']] 
print(len(list))

1. 12
2. 11
3. 6
4. 22

======================================================
q8.
Find the output of the following program: 

list = ['python', 'learning', '@', 'Geeks', 'for', 'Geeks'] 
print(list[0:6:2])

1. ['python', '@', 'for']
2. ['Geeks', 'Geeks', 'learning']
3. ['python', 'learning', '@', 'Geeks', 'for', 'Geeks']
4. ['python', 'Geeks']

======================================================
q9.
Find the output of the following program: 

list = ['a', 'b', 'c', 'd', 'e'] 
print(list[10:] )

1. [\'a\', \'b\', \'c\', \'d\', \'e\']
2. [ \'c\', \'d\', \'e\']
3. [ ]
4. [\'a\', \'b\']

======================================================
q10.
Find the output of the following program: 

list = ['a', 'b', 'c'] * -3
print(list)

1. [\'a\', \'b\', \'c\', \'a\', \'b\', \'c\', \'a\', \'b\', \'c\']
2. [\'c\', \'b\', \'a\', \'c\', \'b\', \'a\', \'c\', \'b\', \'a\']
3. [ ]
4. [\'a\', \'b\', \'c\']

======================================================
q11.
Find the output of the following program: 

L1 = []
L1.append([1, [2, 3], 4]) 
L1.extend([7, 8, 9]) 
print(L1[0][1][1] + L1[2]) 

1. Type Error
2. 12
3. 11
4. 38

======================================================
q12.
Find the output of the following program: 

L1 = [1, 2, 3, 4] 
L2 = L1 
L3 = L1.copy() 
L4 = L1
L1[0] = [5] 
print(L1, L2, L3, L4) 

1. [5, 2, 3, 4] [5, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]
2. [[5], 2, 3, 4] [[5], 2, 3, 4] [[5], 2, 3, 4] [1, 2, 3, 4]
3. [5, 2, 3, 4] [5, 2, 3, 4] [5, 2, 3, 4] [1, 2, 3, 4]
4. [[5], 2, 3, 4] [[5], 2, 3, 4] [1, 2, 3, 4] [[5], 2, 3, 4]

======================================================
q13.
Which of the following are true for objects of Python’s set type:

1. A given element can’t appear in a set more than once.
2. A set may contain elements that are mutable.
3. The order of elements in a set is significant.
4. Sets are mutable.

======================================================
q14.
Which of the following define the set {'a', 'b', 'c'}:

1. s = ('a', 'b', 'c')
2. s = (['a', 'b', 'c'])
3. s = ('abc')
4. s = {'a', 'b', 'c'}
5. s = {('a', 'b', 'c')}

======================================================
q15.
You have a set s defined as follows:
s = {100, 200, 300}
Which one of the following statements
does not correctly produce the union of s and the set {300, 400, 500}:

1. s | {300, 400, 500}
2. s.union([300, 400, 500])
3. s | set([300, 400, 500])
4. s | [300, 400, 500]
5. s.union(set([300, 400, 500]))
6. s.union({300, 400, 500})

======================================================
q16.
What is the result of this statement:
{1, 2, 3, 4, 5} - {3, 4}

1. {1, 2, 5}
2. {3, 4, 5, 6, 7}
3. set()
4. {1, 2, 6, 7}

======================================================
q17.
What is the result of the highlighted expression:

>>> x = {1, 2, 3}
>>> y = {1, 2}

>>> y.issubset(x)

1. It raises an exception.
2. set()
3. True
4. False

======================================================
q18.
Suppose a set s is defined as follows:
s = {'foo', 'bar', 'baz', 'qux'}
Which of the following remove element 'bar' from s:

1. del s['bar']
2. s.difference_update({'bar'})
3. s.pop()
4. s &= {'foo', 'baz', 'qux'}
5. s -= {'bar'}
6. s.discard('bar')

======================================================
q19.
What is the output of the following program?
tuple = (1, 2, 3, 4) 
tuple.append( (5, 6, 7) ) 
print(len(my_tuple)) 

1. 1
2. 2
3. 5
4. Error

======================================================
q20.
What is the output of the following program?
tuple1 = (1, 2, 4, 3) 
tuple2 = (1, 2, 3, 4) 
print(tuple1 < tuple2) 

1. Error
2. True
3. False
4. Unexpected

======================================================
q21.
What is the output of the following program?
tuple = (1, 2, 3) 
print(2 * tuple) 

1. (1, 2, 3, 1, 2, 3)
2. (1, 2, 3, 4, 5, 6)
3. (3, 6, 9)
4. Error
======================================================
q22.
 What is the output of the following program?
tuple=(\"Check\")*3
print(tuple) 

1. Unexpected
2. 3Check
3. CheckCheckCheck
4. Syntax Error

======================================================
q23.
What is the output of the following program?
T1 = (1) 
T2 = (3, 4) 
T1 += 5 <====> T1 = T1 + 5
print(T1)

1. TypeError
2. (1, 5, 3, 4)
3. 1 TypeError
4. 6

======================================================
q24.
Which of the following are true of Python dictionaries:

1. A dictionary can contain any object type except another dictionary.
2. Dictionaries are mutable.
3. Items are accessed by their position in a dictionary.
4. All the keys in a dictionary must be of the same type.
5. Dictionaries can be nested to any depth.
6. Dictionaries are accessed by key.

======================================================
q25.
d = {'foo': 100, 'bar': 200, 'baz': 300}
What is the result of this statement:
d['bar':'baz']

1. (200, 300)
2. Error
3. 200 300
4. [200, 300]

======================================================
q26.
Suppose x is defined as follows:

x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30                print(x[2]['bar']['z'])
        },
        'baz': 3
    },
    'c',
    'd'
]
What is the expression involving x that accesses the value 30?
======================================================
q27.
Which of the following could be a valid dictionary key:

1. len
2. ('foo', 'bar')
3. 'foo'
4. dict(foo=1, bar=2)
5. (3+2j)
6. ['foo', 'bar']

======================================================
q28.
Consider again this nested structure definition:

x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]
Is the following statement True or False?
'z' in x[2]

1. True

2. False
======================================================
'''