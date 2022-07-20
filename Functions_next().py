# Python next() Function

# Example
# Create an iterator, and print the items one by one:

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

# Definition and Usage
# The next() function returns the next item in an iterator.

# You can add a default return value, to return if the iterable has reached to its end.

# Syntax
# next(iterable, default)

# Parameter Values
# Parameter	                Description
# iterable	                Required. An iterable object.
# default	                Optional. An default value to return if the iterable has reached to its end.

# More Examples
# Example
# Return a default value when the iterable has reached to its end:

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)

