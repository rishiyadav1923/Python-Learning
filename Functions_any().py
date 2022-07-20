# Python any() Function

# Example
# Check if any of the items in a list are True:

mylist = [False, True, False]
x = any(mylist)

# Definition and Usage
# The any() function returns True if any item in an iterable are true, otherwise it returns False.

# If the iterable object is empty, the any() function will return False.

# Syntax
# any(iterable)

# Parameter Values
# Parameter	                    Description
# iterable	                    An iterable object (list, tuple, dictionary)

# More Examples
# Example
# Check if any item in a tuple is True:

mytuple = (0, 1, False)
x = any(mytuple)

# Example
# Check if any item in a set is True:

myset = {0, 1, 0}
x = any(myset)

# Example
# Check if any item in a dictionary is True:

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)

# *Note: When used on a dictionary, the any() function checks if any of the keys are true, not the values.

# Related Pages
# The all() Function