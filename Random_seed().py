# Python Random seed() Method

# Example
# Set the seed value to 10 and see what happens:

import random

random.seed(10)
print(random.random())

# Definition and Usage
# The seed() method is used to initialize the random number generator.
# The random number generator needs a number to start with (a seed value), to be able to generate a random number.
# By default the random number generator uses the current system time.
# Use the seed() method to customize the start number of the random number generator.

# *Note: If you use the same seed value twice you will get the same random number twice. See example below

# Syntax
# random.seed(a, version)

# Parameter Values
# Parameter	                    Description
# a	                            Optional. The seed value needed to generate a random number.
#                               If it is an integer it is used directly, if not it has to be converted into an integer.
#                               Default value is None, and if None, the generator uses the current system time.
# version	                    An integer specifying how to convert the a parameter into a integer.
#                               Default value is 2

# More Examples
# Example
# Demonstrate that if you use the same seed value twice, you will get the same random number twice:

import random

random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

