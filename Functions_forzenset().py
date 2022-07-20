# Python frozenset() Function

# Example
# Freeze the list, and make it unchangeable:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)

# Definition and Usage
# The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).

# Syntax
# frozenset(iterable)

# Parameter Values
# Parameter	                    Description
# iterable	                    An iterable object, like list, set, tuple etc.

# More Examples
# Example
# Try to change the value of a frozenset item.

# This will cause an error:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry"
