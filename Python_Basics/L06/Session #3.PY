""""
=================================
-----> Exceptions Handling <-----
=================================
[1] try => Test the code for errors
[2] except => Handle the errors
# -------------------------------
[3] else => If no errors
[4] finally => Run the code
==================================
"""

# intro. example
# numb = int(input("Enter a number: "))
# print(type(numb))  # If u run this code, an error will occured

# ------------------------------
# now let's solve this problem.

try:  # try the code and test if there is an error
    numb = int(input("Enter a number: "))
    print(type(numb))
    print("This a message from 'try' ")

except:  # if an error appeare, except will handle it
    print("This is not a number!")

else:  # if there is no error, else will continue with code
    # but if u want, u can remove it
    print("This a message from 'else' ")

finally:  # finally will run whatever happens
    print("Any code here will run anyway!!")

# ===================================

# Example
# You can define more than one error by write except more than one time

try:
    age = int(input("Enter ur age: "))
    print(10 / 0)
    # print(a)

except ValueError:
    print("this is not a real number")

except ZeroDivisionError:
    print("You can not divide by zero")

#except NameError:
#    print("This is not defined")

except:
    print("An Error happens")
