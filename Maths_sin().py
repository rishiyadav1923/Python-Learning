# Python math.sin() Method

# Example
# Find the sine of different numbers:

# Import math Library
import math

# Return the sine of different values
print (math.sin(0.00))
print (math.sin(-1.23))
print (math.sin(10))
print (math.sin(math.pi))
print (math.sin(math.pi/2))

# Definition and Usage
# The math.sin() method returns the sine of a number.

# *Note: To find the sine of degrees, it must first be converted into radians with the math.radians() method (see example below).

# Syntax
# math.sin(x)

# Parameter Values
# Parameter	        Description
# x	                Required. The number to find the sine of. If the value is not a number, it returns a TypeError

# Technical Details
# Return Value:	A float value, from -1 to 1, representing the sine of an angle
# Python Version:	1.4
# More Examples
# Example
# Find the sine of different degrees:

# Import math Library
import math

# Return the sine value of 30 degrees
print(math.sin(math.radians(30)))

# Return the sine value of 90 degrees
print(math.sin(math.radians(90)))

