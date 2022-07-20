# Python String join() Method

# Example
# Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# Definition and Usage
# The join() method takes all items in an iterable and joins them into one string.

# A string must be specified as the separator.

# Syntax
# string.join(iterable)

# Parameter Values
# Parameter	            Description
# iterable	            Required. Any iterable object where all the returned values are strings

# More Examples
# Example
# Join all items in a dictionary into a string, using the word "TEST" as separator:

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.

