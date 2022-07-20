# Python math.perm() Method

# Example
# Find the number of ways to choose k things from n items:

# Import math Library
import math

# Initialize the number of items to choose from
n = 7

# Initialize the number of items to choose
k = 5

# Print the number of ways to choose k items from n items
print (math.perm(n, k))

# The result will be:
# 2520

# Definition and Usage
# The math.perm() method returns the number of ways to choose k items from n items with order and without repetition.

# *Note: The k parameter is optional. If we do not provide one, this method will return n! (for example, math.perm(7) will return 5040).

# Syntax
# math.perm(n, k)

# Parameter Values
# Parameter	            Description
# n	                    Required. Positive integers of items to choose from
# k	                    Optional. Positive integers of items to choose

# *Note: If k is greater than n, it returns 0.
# *Note: If n or k are negative, a ValueError occurs. If n or k  are not integers, a TypeError occurs.

# Technical Details
# Return Value:	An int value, representing the number of ways to choose k items from n items with order and without repetition
# Python Version:	3.8

