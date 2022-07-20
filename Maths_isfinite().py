# Python math.isfinite() Method

# Example
# Check whether a value is finite or not:

# Import math Library
import math

# Check whether the values are finite or not
print(math.isfinite(2000))
print(math.isfinite(-45.34))
print(math.isfinite(+45.34))
print(math.isfinite(math.inf))
print(math.isfinite(float("nan")))
print(math.isfinite(float("inf")))
print(math.isfinite(float("-inf")))
print(math.isfinite(-math.inf))
print(math.isfinite(0.0))
# Definition and Usage
# The math.isfinite() method checks whether a number is finite or not.
# This method returns True if the specified number is a finite number, otherwise it returns False.

# Syntax
# math.isfinite(x)

# Parameter Values
# Parameter	        Description
# x	                Required. The value to check. Must be a number (float/integer/infinite/NaN/finite)

# Technical Details
# Return Value:	A bool value, True if x is finite, False if x is either an infinity or a NaN
# Python Version:	New in Python 3.2

