# Python Numbers

# There are three numeric types in Python:

#    int
#    float
#    complex

# Variables of numeric types are created when you assign a value to them:
# Example
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# To verify the type of any object in Python, use the type() function:
# Example
# print(type(x))
# print(type(y))
# print(type(z))

# Int

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# Example

# Integers:
a = 1
b = 35656222554887711
c = -3255522

print(type(a))
print(type(b))
print(type(c))

# Float

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Example

# Floats:
d = 1.10
e = 1.0
f = -35.59

print(type(d))
print(type(e))
print(type(f))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# Example

# Floats:
i = 35e3
j = 12E4
k = -87.7e100

print(type(i))
print(type(j))
print(type(k))

# Complex

# Complex numbers are written with a "j" as the imaginary part:
# Example

# Complex:
l = 3+5j
m = 5j
n = -5j

print(type(l))
print(type(m))
print(type(n))

# Type Conversion

# You can convert from one type to another with the int(), float(), and complex() methods:
# Example

# Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
o = float(x)

#convert from float to int:
p = int(y)

#convert from int to complex:
q = complex(x)

print(o)
print(p)
print(q)

print(type(o))
print(type(p))
print(type(q))

# Note: You cannot convert complex numbers into another number type.
# Random Number

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Example

# Import the random module, and display a random number between 1 and 9:
# import random

import random

print(random.randrange(1, 10))