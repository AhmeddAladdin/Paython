# calculator with function:

def addition(x, y):
    return x+y


def subtract(x, y):
    return x-y


def division(x, y):
    return x/y


def multiplication(x, y):
    return x*y


while True:
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the second number:'))
    operation = int(input('''
1. addition
2. subtract
3. division
4. multiplication
5. exit
--> choose number of the operation:'''))

    if operation in (1, 2, 3, 4, 5):
        if operation == 1:
            print(f'Ans: x + y = {addition(num1,num2)}')
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break
        elif operation == 2:
            print(f'Ans: x - y = {subtract(num1,num2)}')
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break
        elif operation == 3:
            print(f'Ans: x / y = {division(num1,num2)}')
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break
        elif operation == 4:
            print(f'Ans: x * y = {multiplication(num1,num2)}')
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break
        elif operation == 5:
            print('Good bye')
            break

    else:
        print('undefined operation')

# ===========================================================

# Get the area:


def square(s):
    return s * s


def rectangle(l, w):
    return l * w


def triangle(b, h):
    return 0.5 * b * h


while True:
    shape = int(input('''1. square
2. rectangle
3. triangle
4. Exit
Choose the number of the shape:'''))
    print()

    if shape in (1, 2, 3, 4):

        if shape == 1:
            s = float(input("Enter the length of the square:"))
            print(square(s))
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break

        elif shape == 2:
            l = float(input("Enter the length of the rectangle:"))
            w = float(input("Enter the width of the rectangle:"))
            print(rectangle(l, w))
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break

        elif shape == 3:
            b = float(input("Enter the length of the base:"))
            h = float(input("Enter the length of the height:"))
            print(triangle(b, h))
            print()
            a = input('Do you want to continue? (yes or no)')
            if a.capitalize() == 'Yes':
                print()
                continue
            else:
                print('Good bye')
                break
        elif shape == 4:
            print('Good bye')
            break
    else:
        print('Undefined shape, try again')
