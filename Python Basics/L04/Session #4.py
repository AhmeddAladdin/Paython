"""
================================
-----> Function Recursion <-----
================================
"""

a = 'ccchhaiiiirrr'
print(a[1:])

# ====================================
print('=' * 40)
# ====================================

def correctWord(word):

    if len(word) == 1:

        return word

    print(f'Start with => {word}')

    if word[0] == word[1]:  # ccchhaiiirr

        print(f'Before correcting => {word}')

        return correctWord(word[1:])  # chhaiiirr

    print(f'After correcting => {word}')

    return word[0] + correctWord(word[1:])


print(f'Final correct => {correctWord("ccchhaiiiirr")}')
