# Python math.fmod() Method

# Example
# Return the remainder of x/y:

# Import math Library
import math

# Return the remainder of x/y
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))
print(math.fmod(0, 0))

# Definition and Usage
# The math.fmod() method returns the remainder (modulo) of x/y.

# Syntax
# math.fmod(x, y)

# Parameter Values
# Parameter	            Description
# x	                    Required. A positive or negative number to divide
# y	                    Required. A positive or negative number to divide x with

# *Note: If both x and y = 0, it returns a ValueError.
# *Note: If y = 0, it returns a ValueError.
# *Note: If x or y is not a number, it returns a TypeError.

# Technical Details
# Return Value:	A float value, representing the remainder of x/y
# Python Version:	1.4

