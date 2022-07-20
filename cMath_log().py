# Python cmath.log() Method

# Example
# Find the logarithm of a complex value:

#Import cmath Library
import cmath

#print log value of some given parameters
print (cmath.log(1+ 1j))
print (cmath.log(1, 2.5))

# Definition and Usage
# The cmath.log() method returns the logarithm of a complex value.
# With a single argument, this method returns the natural logarithm of that argument with base e.
# With two arguments, this method returns the logarithm of the first argument (x) with the base of the second argument (base).

# Syntax
# cmath.log(x, base)

# Parameter Values
# Parameter	            Description
# x	                    Required. Specifies the value to calculate the logarithm for. 
#                       If the value is 0 or a negative number, it returns a ValueError.
#                       If the value is not a number, it returns a TypeError
# base	                Optional. The logarithmic base to use. Default is 'e'

# Technical Details
# Return Value:	A complex value, representing the natural logarithm of a number, or the logarithm of number to base
# Python Version:	Changed in version 2.4
# Python Changelog:	The base parameter was added

