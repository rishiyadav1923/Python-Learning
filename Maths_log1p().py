# Python math.log1p() Method

# Example
# Find the log(1+number) for different numbers

# Import math Library
import math

# Return the log(1+number) for different numbers
print(math.log1p(2.7183))
print(math.log1p(2))
print(math.log1p(1))

# Definition and Usage
# The math.log1p() method returns log(1+number), computed in a way that is accurate even when the value of number is close to zero.

# Syntax
# math.log1p(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. Specifies the number to process. If the value is a negative number, it returns a ValueError. If the value is not a number, it returns a TypeError

# Technical Details
# Return Value:	A float value, representing the log value of 1+number
# Python Version:	2.6

