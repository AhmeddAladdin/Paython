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