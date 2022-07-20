# Python math.expm1() Method

# Example
# Find the exponential value of a number - 1:

#Import math Library
import math

#Return the exponential value of a number - 1
print(math.expm1(32))
print(math.expm1(-10.89))

# Definition and Usage
# The math.expm1() method returns Ex - 1.
# 'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.
# This function is more accurate than calling math.exp() and subtracting 1.

# Syntax
# math.expm1(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. Specifies the exponent

# Technical Details
# Return Value:	A float value, representing Ex - 1
# Python Version:	2.7

