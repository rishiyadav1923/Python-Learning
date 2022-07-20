# Python math.gamma() Method

# Example
# Find the gamma function of different numbers:

# Import math Library
import math

# Return the gamma function for different numbers
print(math.gamma(-0.1))
print(math.gamma(8))
print(math.gamma(1.2))
print(math.gamma(80))
print(math.gamma(-0.55))

# Definition and Usage
# The math.gamma() method returns the gamma function at a number.
# *Tip: To find the log gamma value of a number, use the math.lgamma() method.

# Syntax
# math.gamma(x)

# Parameter Values
# Parameter	    Description
# x	            Required. A number to find the gamma function for. If the number is a negative integer, it returns a ValueError. If it is not a number, it returns a TypeError.

# Technical Details
# Return Value:	A float value, representing the gamma function at x
# Python Version:	3.2

