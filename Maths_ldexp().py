# Python math.ldexp() Method

# Example
# Return value of x * (2**i):

#Import math Library
import math

#Return value of x * (2**i)
print(math.ldexp(9, 3))
print(math.ldexp(-5, 2))
print(math.ldexp(15, 2))

# Definition and Usage
# The math.ldexp() method returns  x * (2**i) of the given numbers x and i, which is the inverse of math.frexp().

# Syntax
# math.ldexp(x, i)

# Parameter Values
# Parameter	        Description
# x	                Required. A positive or negative number. If the value is not a number, it returns TypeError
# i	                Required. A positive or negative number. If the value is not a number, it returns TypeError

# Technical Details
# Return Value:	The value of x * (2**i)
# Python Version:	2.6

