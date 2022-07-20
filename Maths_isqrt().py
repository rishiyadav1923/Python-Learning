# Python math.isqrt() Method

# Example
# Round a square root number downwards to the nearest integer:

# Import math Library
import math

# Print the square root of different numbers
print (math.sqrt(10))
print (math.sqrt (12))
print (math.sqrt (68))
print (math.sqrt (100))

# Round square root downward to the nearest integer
print (math.isqrt(10))
print (math.isqrt (12))
print (math.isqrt (68))
print (math.isqrt (100))

# Definition and Usage
# The math.isqrt() method rounds a square root number downwards to the nearest integer.
# *Note: The number must be greater than or equal to 0.

# Syntax
# math.isqrt(x)

# Parameter Values
# Parameter	        Description
# x	                Required. The number to round the square root of. If x is negative, it returns a ValueError. If x is not a number, it returns a TypeError

# Technical Details
# Return Value:	An int value, representing the square root of a number, without decimals
# Python Version:	3.8

