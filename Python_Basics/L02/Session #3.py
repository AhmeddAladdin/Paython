'''
========================
-----> While loop <-----
========================

while condition_is_True
    code will run

'''

a = 1
while a <= 10:
    print(a)
    a = a + 1
else: print("Loop is end")

# =======================

# continue..?

x = 1
while x <= 10:
    x = x + 1
    if x == 7:
        continue
    print(x)
print("loop is end")

# =======================

# break..?

x = 1
while x <= 10:
    x = x + 1
    if x == 7:
        break
    print(x)
print("loop is end")

# =======================

# Guess the password game.

print("""=====> Welcome to GUESS THE PASSWORD game <=====
===> you have 5 tries to guess the right pass <===
""")

rightpassword = "apple in basket"
guessing = input("Enter your answer:")
tries = 5

while guessing != rightpassword:
    tries = tries - 1
    if tries == 0:
        print("WRONG!, No more tries, Loser!")
        break
    print("Wrong!, last chance!"if tries == 1 else "Wrong!, {:d} tries left!".format(tries))
    guessing = input("Enter your answer:")

else:
    print("Good Job, winner!")
