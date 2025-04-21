# range()

for x in range(5):
    print(x)

# =======================================
print('=' * 40)
# =======================================

for x in range(1, 10):
    print(x)

# =======================================
print('=' * 40)
# =======================================

for x in range(5):
    for y in range(1, 10):
        print(y)

# =======================================
print('=' * 40)
# =======================================

# end=
for x in range(5):
    for y in range(1, 10):
        print(y, end="!")
else:
    print('end')
# =======================================
print('=' * 40)
# =======================================

for x in range(5):
    for y in range(1, 10):
        print(y, end="!")
    print()  # add new line

# =======================================
print('=' * 40)
# =======================================

# made a shapes

rows = int(input('enter the number of rows:'))
columns = int(input('enter the number of columns:'))
symbol = input('enter a symbol to use:')

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()
