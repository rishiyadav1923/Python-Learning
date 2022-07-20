# Python cmath.isnan() Method

# Example
# Check whether a complex value is NaN or not:

#import cmath for complex number operations
import cmath

#find whether a complex number is NaN or not
print (cmath.isnan(12 + float('nan')))
print (cmath.isnan(2 + 3j))

# Definition and Usage
# The cmath.isnan() method checks whether a value is nan (Not a Number), or not. This method returns a Boolean value: True if the value is nan, otherwise False

# Syntax
# cmath.isnan(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. The value to check for NaN

# Technical Details
# Return Value:	A bool value, True if any part (real or imaginary) of a complex number is NaN, otherwise False
# Python Version:	2.6

