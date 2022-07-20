# Python math.isinf() Method

# Example
# Check whether a value is infinity or not:

# Import math Library
import math

# Check whether the values are infinite or not
print(math.isinf(56))
print(math.isinf(-45.34))
print(math.isinf(+45.34))
print(math.isinf(math.inf))
print(math.isinf(float("nan")))
print(math.isinf(float("inf")))
print(math.isinf(float("-inf")))
print(math.isinf(-math.inf))

# Definition and Usage
# The math.isinf() method checks whether a number is infinite or not.
# This method returns True if the specified number is a positive or negative infinity, otherwise it returns False.

# Syntax
# math.isinf(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. The number to check

# Technical Details
# Return Value:	A bool value, True if x is a positive or negative infinity, False otherwise
# Python Version:	2.6

