# Python cmath.log10() Method

# Example
# Find the base-10 logarithm of a complex number:

#Import cmath Library
import cmath

#print base-10 log value of complex numbers
print (cmath.log10(2+ 3j))
print (cmath.log10(1+ 2j))

# Definition and Usage
# The cmath.log10() method returns the base-10 logarithm of a complex number.
# There is one branch cut, from 0 along the negative real axis to -∞, continuous from above.

# Syntax
# cmath.log10(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. Specifies the value to calculate the base-10 logarithm for. 
#                       If the value is 0 or a negative number, it returns a ValueError. 
#                       If the value is not a number, it returns a TypeError

# Technical Details
# Return Value:	A complex value, representing the base-10 logarithm of a number
# Python Version:	1.5

