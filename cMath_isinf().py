# Python cmath.isinf() Method

# Example
# Check whether a complex value is infinite or not:

#import cmath for complex number operations
import cmath

#find whether a complex number is infinite or not
print (cmath.isinf(complex(10 + float('inf'))))
print (cmath.isinf(11 + 4j))

# Definition and Usage
# The cmath.isinf() method checks whether a value is positive or negative infinity, or not. This method returns a Boolean value: True if the value is infinity, otherwise False.

# Syntax
# cmath.isinf(x)

# Parameter Values
# Parameter	            Description
# x	                    Required. The value to check for infinity

# Technical Details
# Return Value:	A bool value, True if the value is infinity, otherwise False
# Python Version:	2.6

