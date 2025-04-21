# Modulus
print(10 / 3)

# Exponent
print(3 ** 3)

print("=========================")
# =============================

# Project : Check if the number even or odd.

num = int(input("Enter an integer number: "))
remainder = num % 2

if remainder == 0:
    print("{:d} is an \"Even\" number!".format(num))

else:
    print("{:d} is an \"Odd\" number!".format(num))

print("=========================")
# ===================================

# Project: Your age in details v1

age = int(input("Enter your age here: "))
Years = age
Months = Years * 12
Weeks = Months * 4
Days = Years * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60

print('''You lived for:
==> {:d} Years
==> {:d} Months
==> {:d} Weeks
==> {:d} Days
==> {:d} Hours
==> {:d} Minutes
==> {:d} Seconds''' .format(Years, Months, Weeks, Days, Hours, Minutes, Seconds))

print("=========================")
# ===================================