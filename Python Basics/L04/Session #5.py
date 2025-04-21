"""
===========================
-----> File Handling <-----
===========================
=> Modes:
1. 'a' Append: open file for appending values, create file if not exists
2. 'r' Read: [Default value] open file for read and give error if file isn't exists
3. 'w' Write: open file for writing, create file if not exists
4. 'x' Create: create file, give error if not exists
"""

# abspath, relativePath

# abspath
'''myFile1 = open('D:/Python/files/ali.txt')'''

# relativePath
'''myFile2 = open('ali.txt')'''

# os
import os

# Main current worked directory
print(os.getcwd())

# Name of the opened file
print(os.path.abspath(__file__))

# Directory for the opened file
print(os.path.dirname(os.path.abspath(__file__)))

# Change the current worked directory
os.chdir(r'C:\Users\Ahmed\OneDrive\Documents\Python\python course\SmartZone_course\L04')
print(os.getcwd())

myFile = open('Ahmed.txt')

