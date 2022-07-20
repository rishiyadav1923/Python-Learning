# Python iter() Function

# Example
# Create an iterator object, and print the items:

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# Definition and Usage
# The iter() function returns an iterator object.

# Syntax
# iter(object, sentinel)

# Parameter Values
# Parameter	            Description
# object	            Required. An iterable object
# sentinel	            Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel

# Related Pages
# The reversed() function returns a reversed iterator object.


