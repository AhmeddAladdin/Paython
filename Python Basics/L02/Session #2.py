"""
================================
----> Match case statement <----
================================

It is the same as if statement but easier,
and for short states.

================================

variable = "value"

match variable:
    case 1:
        #DO something
    case 2:
        #Do another somthing
    case 3:
        # and the same for other cases.
    case _: # this if like "else", meaning that if all cases isn't true then do this case.
        #Do something

"""
# Ex.1
grade = int(input("Enter Your Grade:"))

match grade:
    case 5:
        print("Excellent")
    case 4:
        print("Very Good")
    case 3:
        print("Good")
    case 2:
        print("Need to improve")
    case 1:
        print("Try again")
    case _:
        print("Undefined Degree")

print("=================================")

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

print("===================================")

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