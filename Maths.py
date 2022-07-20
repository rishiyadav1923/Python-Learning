# Python Math

# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

# Example
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:

# Example
x = abs(-7.25)

print(x)

# The pow(x, y) function returns the value of x to the power of y (xy).

# Example
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)

# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.

# To use it, you must import the math module:

import math

# When you have imported the math module, you can start using methods and constants of the module.
# The math.sqrt() method for example, returns the square root of a number:

# Example
import math

x = math.sqrt(64)

print(x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

# Example
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# The math.pi constant, returns the value of PI (3.14...):

# Example
import math

x = math.pi

print(x)

# Complete Math Module Reference
# In our Math Module Reference you will find a complete reference of all methods and constants that belongs to the Math module.

# Python math Module
# Python has a built-in module that you can use for mathematical tasks.

# The math module has a set of methods and constants.

# Math Methods
# Method	            Description
# math.acos()	        Returns the arc cosine of a number
# math.acosh()	        Returns the inverse hyperbolic cosine of a number
# math.asin()	        Returns the arc sine of a number
# math.asinh()	        Returns the inverse hyperbolic sine of a number
# math.atan()	        Returns the arc tangent of a number in radians
# math.atan2()	        Returns the arc tangent of y/x in radians
# math.atanh()	        Returns the inverse hyperbolic tangent of a number
# math.ceil()	        Rounds a number up to the nearest integer
# math.comb()	        Returns the number of ways to choose k items from n items without repetition and order
# math.copysign()	    Returns a float consisting of the value of the first parameter and the sign of the second parameter
# math.cos()	        Returns the cosine of a number
# math.cosh()	        Returns the hyperbolic cosine of a number
# math.degrees()	    Converts an angle from radians to degrees
# math.dist()	        Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
# math.erf()	        Returns the error function of a number
# math.erfc()	        Returns the complementary error function of a number
# math.exp()	        Returns E raised to the power of x
# math.expm1()	        Returns Ex - 1
# math.fabs()	        Returns the absolute value of a number
# math.factorial()	    Returns the factorial of a number
# math.floor()	        Rounds a number down to the nearest integer
# math.fmod()	        Returns the remainder of x/y
# math.frexp()	        Returns the mantissa and the exponent, of a specified number
# math.fsum()	        Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
# math.gamma()	        Returns the gamma function at x
# math.gcd()	        Returns the greatest common divisor of two integers
# math.hypot()	        Returns the Euclidean norm
# math.isclose()	    Checks whether two values are close to each other, or not
# math.isfinite()	    Checks whether a number is finite or not
# math.isinf()	        Checks whether a number is infinite or not
# math.isnan()	        Checks whether a value is NaN (not a number) or not
# math.isqrt()	        Rounds a square root number downwards to the nearest integer
# math.ldexp()	        Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
# math.lgamma()	        Returns the log gamma value of x
# math.log()	        Returns the natural logarithm of a number, or the logarithm of number to base
# math.log10()	        Returns the base-10 logarithm of x
# math.log1p()	        Returns the natural logarithm of 1+x
# math.log2()	        Returns the base-2 logarithm of x
# math.perm()	        Returns the number of ways to choose k items from n items with order and without repetition
# math.pow()	        Returns the value of x to the power of y
# math.prod()	        Returns the product of all the elements in an iterable
# math.radians()	    Converts a degree value into radians
# math.remainder()	    Returns the closest value that can make numerator completely divisible by the denominator
# math.sin()	        Returns the sine of a number
# math.sinh()	        Returns the hyperbolic sine of a number
# math.sqrt()	        Returns the square root of a number
# math.tan()	        Returns the tangent of a number
# math.tanh()	        Returns the hyperbolic tangent of a number
# math.trunc()	        Returns the truncated integer parts of a number

# Math Constants
# Constant	            Description
# math.e	            Returns Euler's number (2.7182...)
# math.inf	            Returns a floating-point positive infinity
# math.nan	            Returns a floating-point NaN (Not a Number) value
# math.pi	            Returns PI (3.1415...)
# math.tau	            Returns tau (6.2831...)