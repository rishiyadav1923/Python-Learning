# Python Random triangular() Method

# Example
# Return a random number between, and included, 20 and 60, but most likely closer to 20:

import random

print(random.triangular(20, 60, 30))

# Definition and Usage
# The triangular() method returns a random floating number between the two specified numbers (both included), but you can also specify a third parameter, the mode parameter.
# The mode parameter gives you the opportunity to weigh the possible outcome closer to one of the other two parameter values.
# The mode parameter defaults to the midpoint between the two other parameter values, which will not weigh the possible outcome in any direction.

# Syntax
# random.triangular(low, high, mode)

# Parameter Values
# Parameter	                    Description
# low	                        Optional. A number specifying the lowest possible outcome.
#                               Default 0
# high	                        Optional. A number specifying the highest possible outcome.
#                               Default 1
# mode	                        Optional. A number used to weigh the result in any direction.
# Default                       the midpoint between the low and high values

