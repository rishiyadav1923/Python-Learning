# Python del Keyword

# Example
# Delete an object:

class MyClass:
  name = "John"

del MyClass

print(MyClass)

# Definition and Usage
# The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.

# More Examples
# Example

# Delete a variable:

x = "hello"

del x

print(x)

# Example
# Delete the first item in a list:

x = ["apple", "banana", "cherry"]

del x[0]

print(x)

