# Python cmath.isclose() Method

# Example
# Compare the closeness of two complex values:

#Import cmath Library
import cmath

#compare the closeness of two complex values using relative tolerance
print(cmath.isclose(10+5j, 10+5j))
print(cmath.isclose(10+5j, 10.01+5j))

# Definition and Usage
# The cmath.isclose() method checks whether two complex values are close, or not. This method returns a Boolean value: True if the values are close, otherwise False.
# This method uses a relative tolerance, or an absolute tolerance, to see if the values are close.

# *Tip: It uses the following formula to compare the values:
# abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# Syntax
# cmath.isclose(a, b, rel_tol = value, abs_tol = value)

# Parameter Values
# Parameter	            Description
# a	                    Required. The first value to check for closeness
# b	                    Required. The second value to check for closeness
# rel_tol = value	    Optional. The relative tolerance. It is the maximum allowed difference between value a and b.
#                       Default value is 1e-09
# abs_tol = value	    Optional. The minimum absolute tolerance. It is used to compare values near 0. 
#                       The value must be at least 0

# Technical Details
# Return Value:	A bool value. True if the values are close, otherwise False
# Python Version:	3.5

# More Examples
# Example
# Compare the closeness of two complex values where absolute tolerance is defined:

#Import cmath Library
import cmath

#compare the closeness of two complex values using absolute tolerance
print(cmath.isclose(10+5j, 10+5j, abs_tol=0.005))
print(cmath.isclose(10+5j, 10.01+5j, abs_tol=0.005))

