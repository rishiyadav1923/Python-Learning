# Python sorted() Function

# Example
# Sort a tuple:

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

# Definition and Usage
# The sorted() function returns a sorted list of the specified iterable object.
# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

# *Note: You cannot sort a list that contains BOTH string values AND numeric values.

# Syntax
# sorted(iterable, key=key, reverse=reverse)

# Parameter Values
# Parameter             	Description
# iterable	                Required. The sequence to sort, list, dictionary, tuple etc.
# key	                    Optional. A Function to execute to decide the order. Default is None
# reverse	                Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

# More Examples
# Example
# Sort numeric:

a = (1, 11, 2)
x = sorted(a)
print(x)

# Example
# Sort ascending:

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
print(x)

# Example
# Sort descending:

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

