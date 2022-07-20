# Python math.lgamma() Method

# Example
# Find the log gamma value of different numbers:

# Import math Library
import math

# Return the log gamma value of different numbers
print (math.lgamma(7))
print (math.lgamma(-4.2))

# Definition and Usage
# The math.lgamma() method returns the natural logarithm gamma value of a number.
# *Tip: We can find also find the log gamma value by using the math.gamma() method to find the gamma value, and then use the math.log() method to calculate the log of that value.
# *Tip: The gamma value is equal to factorial(x-1).

# Syntax
# math.lgamma(x)

# Parameter Values
# Parameter	        Description
# x	                Required. The number to find the log gamma value of. If the number is a negative integer, it returns a ValueError. If it is not a number, it returns a TypeError.

# Technical Details
# Return Value:	A float value, representing the log gamma value of a number
# Python Version:	3.2

