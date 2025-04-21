"""
=====================
-----> Turtle <-----
=====================
==>> Out lines
- intro.
- regular shapes
- loops in turtle
- func. in turtle
"""
from turtle import *

# regular shapes:
# square:

x = Turtle()
x.forward(200)  # first line
x.left(90)  # rotate turtle
x.forward(200)   # Second line
x.left(90)  # rotate turtle
x.forward(200)  # third line
x.left(90)  # rotate turtle
x.forward(200)  # fourth line
x.left(90)  # rotate turtle

done()

# ======================================

# loops in turtle
# square by for loop

from turtle import *

y = Turtle()
for i in range(4):

    y.forward(200)
    y.left(90)

done()

# =======================================

# Ex: draw a triangle

from turtle import *

y = Turtle()
for i in range(3):

    y.forward(200)
    y.left(120)

done()

# ========================================

# using func.

def shapes(t, n, length):
    for i in range(n):
        t.forward(length)
        t.left(360/n)

from turtle import *

x = Turtle()
shapes(x, 5, 100)
done()

# ========================================

# adding color:

def shapes(t, n, length):
    for i in range(n):
        t.forward(length)
        t.left(360/n)

from turtle import *

x = Turtle()
x.color('red', 'orange')
x.begin_fill()
x.pensize(5)

shapes(x, 5, 100)

x.end_fill()
done()

# ========================================

# sin() in math

from turtle import *
from math import *

x = Turtle()
x.speed(0)  # 0:fastest, 10:fast, 6:normal, 3:slow, 1:slowest
for i in range(2000):
    x.forward(10)
    x.left(sin(i/10)*25)
    x.left(20)

done()