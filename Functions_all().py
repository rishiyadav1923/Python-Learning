# Python all() Function

# Example
# Check if all items in a list are True:

mylist = [True, True, True]
x = all(mylist)

# Definition and Usage
# The all() function returns True if all items in an iterable are true, otherwise it returns False.

# If the iterable object is empty, the all() function also returns True.

# Syntax
# all(iterable)

# Parameter Values
# Parameter	                    Description
# iterable	                    An iterable object (list, tuple, dictionary)

# More Examples
# Example
# Check if all items in a list are True:

mylist = [0, 1, 1]
x = all(mylist)

# Example
# Check if all items in a tuple are True:

mytuple = (0, True, False)
x = all(mytuple)

# Example
# Check if all items in a set are True:

myset = {0, 1, 0}
x = all(myset)

# Example
# Check if all items in a dictionary are True:

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)

# *Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.

# Related Pages
# The any() Function

