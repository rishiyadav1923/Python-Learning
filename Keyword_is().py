# Python is Keyword

# Example
# Check if two objects are the same object:

x = ["apple", "banana", "cherry"]

y = x

print(x is y)

# Definition and Usage
# The is keyword is used to test if two variables refer to the same object.
# The test returns True if the two objects are the same object.
# The test returns False if they are not the same object, even if the two objects are 100% equal.
# Use the == operator to test if two variables are equal.

# More Examples
# Example
# Test two objects that are equal, but not the same object:

x = ["apple", "banana", "cherry"]

y = ["apple", "banana", "cherry"]

print(x is y)

