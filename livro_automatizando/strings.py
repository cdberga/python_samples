"""Este é um programa Python para testes.
Criado por Al Sweigart al@inventwithpython.com
Esse programa foi criado para Python 3, e não para Python 2.
"""

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,

Bob''')

print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())

print(','.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())

print('Hello'.rjust(10))
print('World'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))

print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))

spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
