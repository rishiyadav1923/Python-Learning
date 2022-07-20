# Python Random sample() Method

# Example
# Return a list that contains any 2 of the items from a list:

import random

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))

# Definition and Usage
# The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.

# *Note: This method does not change the original sequence.

# Syntax
# random.sample(sequence, k)

# Parameter Values
# Parameter	                Description
# sequence	                Required. A sequence. Can be any sequence: list, set, range etc.
# k	                        Required. The size of the returned list

