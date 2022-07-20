# Python math.isnan() Method

# Example
# Check whether a value is NaN or not:

# Import math Library
import math

# Check whether some values are NaN or not
print (math.isnan (56))
print (math.isnan (-45.34))
print (math.isnan (+45.34))
print (math.isnan (math.inf))
print (math.isnan (float("nan")))
print (math.isnan (float("inf")))
print (math.isnan (float("-inf")))
print (math.isnan (math.nan))

# Definition and Usage
# The math.isnan() method checks whether a value is NaN (Not a Number), or not.
# This method returns True if the specified value is a NaN, otherwise it returns False.

# Syntax
# math.isnan(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. The value to check

# Technical Details
# Return Value:	A bool value, True if the value is NaN, otherwise False
# Python Version:	3.5

