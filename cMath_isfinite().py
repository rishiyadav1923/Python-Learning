# Python cmath.isfinite() Method

# Example
# Check whether a complex value is finite or not:

#import cmath for complex number operations
import cmath

#find whether a complex number is finite or not
print (cmath.isfinite(2 + 3j))
print (cmath.isfinite(complex(5.0,float('inf'))))
print (cmath.isfinite(float('inf')+ 5j))

# Definition and Usage
# The cmath.isfinite() method checks whether a complex value is finite, or not. This method returns a Boolean value: True if the value is finite, otherwise False.

# Syntax
# cmath.isfinite(x)
# Parameter Values

# Parameter	            Description
# x	                    Required. The value to check if it is finite or not

# Technical Details
# Return Value:	A bool value, True if the value is finite, otherwise False
# Python Version:	3.2

