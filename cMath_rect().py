# Python cmath.rect() Method

# Example
# Convert polar coordinates to rectangular form:

#import cmath for complex number operations
import cmath

#convert a polar coordinate to rectangular form
print(cmath.rect(3.1622776601683795, 1.2490457723982544))

# Definition and Usage
# The cmath.rect() method converts polar coordinates to rectangular form of the complex number. It creates a complex number with phase and modulus.
# This method is equivalent to r * (math.cos(phi) + math.sin(phi)*1j).

# *Note: The radius r is the length of the vector, and phi (phase angle) is the angle made with the real axis.

# Syntax
# cmath.rect(r, phi)

# Parameter Values
# Parameter	        Description
# r	                Required. Represents the modulus of a complex number
# phi	            Required. Represents the phase of a complex number

# Technical Details
# Return Value:	A complex value, representing the rectangular form of a complex number
# Python Version:	2.6

