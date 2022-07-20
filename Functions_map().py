# Python map() Function

# Example
# Calculate the length of each word in the tuple:

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

# Definition and Usage
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax
# map(function, iterables)

# Parameter Values
# Parameter	                Description
# function	                Required. The function to execute for each item
# iterable	                Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

# More Examples
# Example

# Make new fruits by sending two iterable objects into the function:

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

