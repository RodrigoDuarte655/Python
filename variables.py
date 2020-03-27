# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'John'   # str
# is_cool = True  # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)

#1001

A = int(input(''))
B = int(input(''))

X = (A + B)

print('X = ' + str(X))
print('X = {X}'.format(X = X))
print(f'X = {X}')

print(type(X))

#1002

n = 3.14159

R = float(input(''))

A = (n * (R*R))

print("A={:.4f}".format(A))

#1003
A = int(input())
B = int(input())

SOMA = A + B

print('SOMA = {}'.format(SOMA))

#1004
a = int(input())
b = int(input())

PROD = a * b

print('PROD = {}'.format(PROD))