"""
1- if inside if
2- if and print in the same line
3- short if
"""
# 1- if inside if

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

# =======================================================

# 2- if and print in the same line

temp = int(input("enter the degree: "))
if temp >= 20 and temp <= 30 : print("good")
else : print("bad")

# =======================================================

# 3- short if

degree = float(input("enter the degree: "))
print("Successful" if degree >= 49.5 and degree <= 100 else "failed" )

# =======================================================