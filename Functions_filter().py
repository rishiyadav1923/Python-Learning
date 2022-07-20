# Python filter() Function

# Example
# Filter the array, and return a new array with only the values equal to or above 18:

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

# Definition and Usage
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

# Syntax
# filter(function, iterable)

# Parameter Values
# Parameter	            Description
# function	            A Function to be run for each item in the iterable
# iterable	            The iterable to be filtered

