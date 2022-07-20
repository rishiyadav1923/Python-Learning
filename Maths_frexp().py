# Python math.frexp() Method

# Example
# Find the mantissa and exponent of a number:

#Import math Library
import math

#Return mantissa and exponent of numbers
print(math.frexp(4))
print(math.frexp(-4))
print(math.frexp(7))

# Definition and Usage
# The math.frexp() method returns the mantissa and the exponent of a specified number, as a pair (m,e).
# The mathematical formula for this method is: number = m * 2**e.

# Syntax
# math.frexp(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. A positive or negative number. If the value is not a number, it returns TypeError

# Technical Details
# Return Value:	A tuple value, representing the mantissa and exponent of x, as a pair (m,e). Mantissa is returned as float exponent returned as integer
# Python Version:	2.6

