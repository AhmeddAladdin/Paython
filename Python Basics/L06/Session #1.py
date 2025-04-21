""""
========================
-----> Decorators <-----
========================
[1] Sometimes called 'Meta programming'
[2] Everything in python is 'object'
[3] Decorator take a function, add some functionality, then return it
[4] Decorator affect on other functions and enhance their behavior
[5] Decorator is a higher order function (function accept another function as a parameter)
========================
"""

# First: if function does not have parameters

# انشاء الديكوريتور
def mydecorator(the_func):

    def decoration(): # سميها اي اسم، دي بس عشان الديكوريشن اللي هيتعمل

        print("Welcome to Egypt!") # دا ديكور
        
        the_func() # دي بتعبر عن الداله اللي هيتعملها ديكوريت

        print("Good bye!") # دا ديكور

    return decoration


# الداله المراد عملها ديكوريشن
def Example_1():

    print("We hope that you are enjoing our country <3")


# الطريقه الاولى لعمل ديكوريشن
print("=" * 50)

Example_1()

print("=" * 50)

after_decoration = mydecorator(Example_1)
after_decoration()

print("=" * 50)

# الطريقه الثانية
@mydecorator
def Example_2():

    print("We are happy to see you here!")

Example_2()

print("=" * 50)

# ===========================================

# Second: if function has parameters.

def decorator_2(the_func):

    def decoration(p1, p2):

        print("Welcome to Egypt!")
        
        the_func(p1, p2)

        print("Good bye!")

    return decoration

# Example 1
@decorator_2
def first(person1, person2):

    print(f'Hello {person1} and {person2}.')

first("Ahmed", "Ali")

print("=" * 50)

# ===

# Advanced Example
def check_on_calculation(func):

    def processor(n1, n2):

        print("Let's calculate this numbers!")

        print("the result =", end=" "), func(n1, n2)

        if n1 < 0 or n2 < 0:
            print("The sum decreased as there is a negative number.")


    return processor

# ===

@check_on_calculation
def sum(num1, num2):

    print(num1 + num2)


sum(-10, 12)

print("=" * 50)

# ==========================================

# you can use more than one decorator on the same function
# we will apply on the same example

def check_on_calculation(func):

    def processor(n1, n2):

        print("Let's calculate this numbers!")

        func(n1, n2)

        if n1 < 0 or n2 < 0:
            print("The sum decreased as there is a negative number.")

    return processor


def check_on_calculation_Two(func):

    def processor(n1, n2):

        func(n1, n2)

        print("this is another decorator")

    return processor

# ===

@check_on_calculation
@check_on_calculation_Two
def sum(num1, num2):

    print(num1 + num2)


sum(-10, 12)

print("=" * 50)

# =========================================

# What if you add another parameter?!

def check_on_calculation_three(func):

    def processor(*numbers):

        print("Let's calculate this numbers!")

        func(*numbers)

        for i in numbers:
            if i < 0:
                print("The sum decreased as there is a negative number.")


    return processor

# ===

@check_on_calculation_three
def sum(num1, num2, num3, num4):

    print(num1 + num2 + num3 + num4)


sum(121, 3, -10, 12)

print("=" * 50)

# ==========================================

# make a decorator to calculate the run time of any code

from time import time

def runTime(func):

    def counter():

        start = time()

        func()

        end = time()

        print(f"the run time of this code = {end - start}")
    
    return counter


@runTime
def anyfunc():

    for i in range(1, 1001):
        print(i)

anyfunc()

print("=" * 50)

# The END, thanks <3