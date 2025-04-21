# Project [1]: Test the temperature:

temp = int(input("enter the degree: "))
if temp >= 20 and temp <= 30:
    print("good")
else:
    print("bad")

# ===================================

# Project [2]:Test student degree:

degree = float(input("enter the degree: "))
if degree >= 49.5 and degree <= 100:
    print("Successful")
else:
    print("Failed")

# ===================================

# Project [3]:Registration for an app:

Fname = input("Enter your name: ")
Mname = input("Enter your middel name: ")
Lname = input("Enter your last name: ")
age = int(input("Enter your age: "))

Fname = Fname.strip().title()
Mname = Mname.strip().title()
Lname = Lname.strip().title()
age = age

print("Hello %s %s %s I'm happy to see you.\n%d is your age" % (Fname, Mname, Lname, age))

# ===================================

# Project [4]:Personal data registration program:

a = input('Enter your name:')
b = input('Enter your gender:')
c = int(input('Enter your age:'))
d = input('Enter your city:')
e = input('Enter your country:')
f = input('Enter your hobby:')
print('''This is your data
Name: %s
Gender: %s
Age: %d years old
Address: %s, %s
My hobby is: %s''' % (a, b, c, d, e, f))

# ===================================

# Project [5]: Apply in course with discount.

name = 'Ahmed'
country = 'Egypt'
course = 'python course'
price = 100

if country == "Egypt" or country == 'KSA' :
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 80))

elif country == "Kuwait" or country == 'Emirates':
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 60))

else:
    print("Hello %s from %s, \"%s\" price = $%d" % (name, country, course, price - 30))

# ===================================

# Project [6]: Apply in course with discount. (Advanced)

name = input("Enter your name: ")
student = input("Are You student? (Yes or No):")
country = input("Enter your country: ")
course = input("Enter the course you want: ")
price = 150

name = name.strip().title()
student = student.strip().title()
country = country.strip().title()
course = course.strip().title()

if student != 'Yes' or student != 'No':
    print("Error at \"Are You student? (Yes or No)\"\nyou must just answer with (Yes or No)")
else:

    if country == "Egypt" or country == 'KSA':

        if student == 'Yes':
            print("Hello %s from %s, because you're student, the price of your course: \"%s\" = %d" % (
                name, country, course, price - 0.90*price))
        else:
            print("Hello %s from %s, the price of your course: \"%s\" = %d" % (
                name, country, course, price - 0.80*price))

    elif country == "Kuwait" or country == 'Emirates':

        if student == 'Yes':
            print("Hello %s from %s, because you're student, the price of your course: \"%s\" = %d" % (
                name, country, course, price - .55*price))
        else:
            print("Hello %s from %s, the price of your course: \"%s\" = %d" % (
                name, country, course, price - 0.50*price))

    else:
        if student == 'Yes':
            print("Hello %s from %s, because you're student, the price of your course: \"%s\" = %d" % (
            name, country, course, price - 0.30*price))
        else:
            print("Hello %s from %s, the price of your course: \"%s\" = %d" % (
                name, country, course, price - 0.25*price))

# ===================================

# Project [7]: Check if the number even or odd.

num = int(input("Enter an integer number: "))
remainder = num % 2

if remainder == 0:
    print("{:d} is an \"Even\" number!".format(num))

else:
    print("{:d} is an \"Odd\" number!".format(num))

# ===================================

# Project [8]: Body Mass Index (BMI).

mass = float(input("Enter your weight(kg):"))
tall = float(input("Enter your height(cm):"))
operator = mass / ((tall/100)**2)

if operator < 18.5:
    print("BMI = {:f}, Underweight".format(operator))

elif operator >= 18.5 and operator < 25 :
    print("BMI = {:f}, Healthy".format(operator))

elif operator >= 25 and operator < 30 :
    print("BMI = {:f}, Overweight".format(operator))

else:
    print("BMI = {:f}, Obese".format(operator))

# ===================================

# Project [9]: Your age in details

age = int(input("Enter your age here: "))
Years = age
Months = Years * 12
Weeks = Months * 4
Days = Years * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60
print('''You lived for:
%d Years
%d Months
%d Weeks
%d Days
%d Hours
%d Minutes
%d Seconds''' % (Years, Months, Weeks, Days, Hours, Minutes, Seconds))

# ===================================

# Project [10]: Your age in details v2

age = int(input("Enter your age:"))

unit = input("""Choose a unit:
(Years, Months, Weeks, Days, Hours, Minutes, Seconds)
or
(Y, Mon, W, D, H, Min, S):""").strip().capitalize()

Months = age * 12
Weeks = Months * 4
Days = Weeks * 7
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60

if unit == "Years" or unit == "Y":
    print("You lived for '{:d} years'".format(age))

elif unit == "Months" or unit == "Mon":
    print("You lived for '{:d} months'".format(Months))

elif unit == "Weeks" or unit == "W":
    print("You lived for '{:d} weeks'".format(Weeks))

elif unit == "Days" or unit == "D":
    print("You lived for '{:d} days'".format(Days))

elif unit == "Hours" or unit == "H":
    print("You lived for '{:d} hours'".format(Hours))

elif unit == "Minutes" or unit == "Min":
    print("You lived for '{:d} minutes'".format(Minutes))

elif unit == "Seconds" or unit == "S":
    print("You lived for '{:d} seconds'".format(Seconds))

else:
    print("Undefined unit")

# ===================================

# Project [11]: Calculator with if statement

digit_1 = float(input("Enter the first number:"))
operator = input("Choose an operator (+, -, *, /, %, **):")
digit_2 = float(input("Enter the second number:"))

if operator == "+":
    print(digit_1 + digit_2)

elif operator == "-":
    print(digit_1 - digit_2)

elif operator == "*":
    print(digit_1 * digit_2)

elif operator == "/":
    print(digit_1 / digit_2)

elif operator == "**":
    print(digit_1 ** digit_2)

elif operator == "%":
    print(digit_1 % digit_2)

else:
    print("Unknown Operator")

# ===================================

# Project [12]: Calculator with match case statement

digit_1 = float(input("Enter the first number:"))
operator = input("Choose an operator (+, -, *, /, %, **):")
digit_2 = float(input("Enter the second number:"))

match operator:

    case "+":
        print(digit_1 + digit_2)

    case "-":
        print(digit_1 - digit_2)

    case "*":
        print(digit_1 * digit_2)

    case "/":
        print(digit_1 / digit_2)

    case "**":
        print(digit_1 ** digit_2)

    case "%":
        print(digit_1 % digit_2)

    case _:
        print("Unknown Operator")

# ===================================