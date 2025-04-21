""""
==================================
--> Error & Exceptions Raising <--
==================================
[1] Exception gives you the message to understand the problem
[2] Traceback gives you the line to look for the error in this line
[3] Exceptions have types (SyntaxError, IndexError, KeyError, ETC...)
[4] Raise keyword used to raise your own exceptions
==================================
"""

name = input("Enter your name: ")

if type(name) == str:

    print(f"Your name is {name}")

else:

    print(f"{name} is not valid")

print("As you see, the programme is continue")

# =================================================

#print(Ahmed")
#print(21/0)
#print("Ahmed" + 7)

# =================================================

name = input("Enter your name: ")

if type(name) != str:

    raise Exception("You enter a number, please enter your real name")

    print(f"Your name is {name}")

else:

    print(f"{name} is valid")

print("As you see, the programme is continue")