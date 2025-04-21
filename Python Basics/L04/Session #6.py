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

# Reading files

myFile = open(r'D:\Python\files\Ahmed.txt', 'r')

print(myFile)  # return data object not the content.

# Details of data object.
print(myFile.name)
print(myFile.encoding)
print(myFile.mode)

# reading content
print(myFile.read())  # leave it empty and it will return all content
print(myFile.read(5))  # or put number of letters that you want to return

# read line
print(myFile.readline())  # will return 1 line
print(myFile.readline())  # will return the next line
print(myFile.readline(5))  # will return 5 letters only
print(myFile.readline(5))  # will return the next 5 letters

# read lines
print(myFile.readlines())  # will return all lines in list
print(myFile.readlines(50))  # will return 50 letters in list
print(type(myFile.readlines()))  # list

# practice: reading by for loop
for line in myFile:

    print(line)

    if line.startswith('I live'):

        break

# When you finish, close your file.
myFile.close()

# ============================================
print('=' * 40)
# ============================================

# writing in files

MYFile = open(r'D:\Python\files\Dr_Codes.txt', 'w')
MYFile.write("Hello Ahmed\n")
MYFile.write("Hello Omar\n")
# MYFile.write("Hello Ahmed\n" * 500)

# Add list items to a file
file3 = open(r'D:\Python\files\test1.txt', 'w')
list1 = ['Ahmed\n', 'Yousef\n', 'Omar\n']
file3.writelines(list1)

# ============================================
print('=' * 40)
# ============================================

# Append

file3 = open(r'D:\Python\files\test1.txt', 'a')
file3.write('New line\n')
file3.write('Another New line')

# ============================================
print('=' * 40)
# ============================================

# Important Info.

# truncate
file4 = open(r'D:\Python\files\test1.txt', 'a')
file4.truncate(20)

# tell
file4 = open(r'D:\Python\files\test1.txt', 'a')
print(file4.tell())

# seek
file4 = open(r'D:\Python\files\test1.txt', 'a')
file4.seek(6)
print(file4.read())
