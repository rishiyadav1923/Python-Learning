# Python cmath.asinh() Method

# Example
# Find the hyperbolic arc sine of a complex number:

#import cmath for complex number operations
import cmath

#find the hyperbolic arc sine of a complex number
print (cmath.asinh(2+3j))

# Definition and Usage
# The cmath.asinh() method returns the inverse hyperbolic sine of a number.
# There are mainly two branch cuts:

# Extending from 1j along the imaginary axis to ∞j towards the right
# Extending from -1j along the imaginary axis to -∞j towards left

# Syntax
# cmath.asinh(x)

# Parameter Values
# Parameter	                    Description
# x	                            Required. The number to find the inverse hyperbolic sine of

# Technical Details
# Return Value:	A complex value, representing inverse hyperbolic sine of a complex number
# Changelog:	2.6 - Branch cuts are selected according to C99 standard

