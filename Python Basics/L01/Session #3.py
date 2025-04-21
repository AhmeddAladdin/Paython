""""
-----------------------------
--------Concatenation--------
-----------------------------
بستخدمها لربط بين المتغيرات وبعضها
link among strings to make a big one
---------------------------------------
"""
var1 = "My"
var2 = "Name"
var3 = "Ahmed"
print(var1 + var2 + var3) #نلاحظ ان مفيش مسافه بينهم
# ----------------------------------------
# 3 ways to put space
# [1] put space after the word
msg = "My "
gbg = "Name "
pht = "Ahmed"
print(msg + gbg + pht)

# [2] put space before the word
msg = "My"
gbg = " Name"
pht = " Ahmed"
print(msg + gbg + pht)

# [3] space is a character so add it by +
msg = "My"
gbg = "Name"
pht = "Ahmed"
space = " "
print(msg + space + gbg + space + pht)
# -----------------------------------------
# ممكن اعمل متغير زياده و يكون محتواه الربط و اطبعه بسهوله
msg = "My"
gbg = "Name"
pht = "Ahmed"
full = msg + " " + gbg + " " + pht
print(full)
# -----------------------------------------
# concatenation & back slash
a = "one two three\nfour five six"

print(a + " " + b)
print(a )
# -----------------------------------------
# can only link str + str , cannot link str + num
""" print("hello world" + 10) #Error """

"""===========================
--------->Numbers<---------
==========================="""

# integer
print(type(1))
print(type(12))
print(type(-23))
print(type(-1000))

# float
print(type(1.3))
print(type(12.4403))
print(type(-10.43))
print(type(-153.0039))

# complex هو خاص بالهندسه و مش هتلاقي ناس كتير بتتكلم عليه اللى لو في امثله عمليه
c = 5+3j
print(type(c))
print(c)
print(c.real)
print(c.imag)

"""
1.you can convert from int to float and complex
2.you can convert from float to int and complex
3.you cannot convert from complex to others
"""

print(23)
print(float(23))  # convert from int to decimal
print(complex(23))  # convert from int to complex

print(61.054)
print(int(61.054))  # from decimal to int
print(complex(61.054))  # from decimal to complex

# some functions about numbers
mynum = 4
print(str(mynum) + ' is my fav num')  # حل مشكلة الربط بين string and number

print(abs(-5))  # absolute = القيمه المطلقه

print(pow(10,100))  # power = الاس

print(max(3,9,84,12,54))  # يطلع اكبر قيمه
print(min(3,9,84,12,54))  # يطلع اصغر قيمه

print(round(4.8))  # بيقرب الى اقرب رقم صحيح
print(round(4.2))

"""
========================================
--------->Arithmetic Operators<---------
========================================
[+] Addition
[-] Subtraction
[*] Multiplication
[/] Division
[%] Modulus
[**] Exponent
[//] Floor Division
==========================================
"""
# Addition
a, b = 2, 3
print(a + b)
print(-3 + 5)
print(-54 + -23)
print(1.22 + 3.33)

# Subtraction
print(5 - 2)
print(-2 - 4)
print(-1 - -4)
print(-1.23 - 4.32)

# Multiplication
print(2 * 3)
print(-4 * 2)
print(2 * 3 + 4 - 10)

# Division
print(50 / 2)

# Modulus
print(10 % 3)

# Exponent
print(3 ** 2)

# Floor Division
print(100 // 20)
print(115 // 20)
print(120 // 20)

"""
=======================================
----------->Logic Operators<-----------
=======================================
1. (and) : checks two or more conditions if true
2. (or) : checks if at least one condition is true
3. (not) : checks if condition is false
======================================= 
"""
# 1. (and)
x, y, z = 15, 12, 8
if x > y and y > z:
    print("x is the largest number")
else:
    print("x is not the largest number")

# 2. (or)
x, y, z = 15, 12, 8
if x > y or x > z:
    print("x is at least larger than one number")
else:
    print("x is the smallest number")

# 3. (not)
x, y, z = 15, 12, 8
if not (x > y and x > z):
    print("x is the smallest number")
else:
    print("x is the largest number")