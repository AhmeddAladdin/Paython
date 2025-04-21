"""
=====================
-----> Modules <-----
=====================
[1] Module is a python file contain a set of functions
[2] u can module in your app to help u in ur app
[3] u can import multiple modules
[4] u can create ur own module
[5] modules saves ur time
=============================================
"""

# How can I use it?
# ur own module

import tryModules

print(tryModules.checkNum(4))

########################################
print('=' * 40)
########################################
# another module

import random

print(f'This is a random number = {random.random()}')

########################################
print('=' * 40)
########################################

# how to know all func. in the module
# dir()
import random

print(dir(random))

########################################
print('=' * 40)
########################################

# import one or two functions from module

from random import randint

print(f'this is a random number = {randint(100, 500)}')

#############################################
