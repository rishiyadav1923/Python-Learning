# Python Random choice() Method

# Example
# Return a random element from a list:

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

# Definition and Usage
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

# Syntax
# random.choice(sequence)

# Parameter Values
# Parameter	                Description
# sequence	                Required. A sequence like a list, a tuple, a range of numbers etc.

# More Examples
# Example
# Return a random character from a string:

import random

x = "WELCOME"

print(random.choice(x))
