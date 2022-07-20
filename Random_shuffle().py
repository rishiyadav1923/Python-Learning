# Python Random shuffle() Method

# Example
# Shuffle a list (reorganize the order of the list items):

import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

# Definition and Usage
# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.

# *Note: This method changes the original list, it does not return a new list.

# Syntax
# random.shuffle(sequence, function)

# Parameter Values
# Parameter	                    Description
# sequence	                    Required. A sequence.
# function	                    Optional. The name of a function that returns a number between 0.0 and 1.0.
#                               If not specified, the function random() will be used

# More Examples
# Example
# You can define your own function to weigh or specify the result.
# If the function returns the same number each time, the result will be in the same order each time:

import random

def myfunction():
  return 0.1

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist, myfunction)

print(mylist)

