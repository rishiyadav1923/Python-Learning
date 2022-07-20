# Python issubclass() Function

# Example
# Check if the class myObj is a subclass of myAge:

class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)

# Definition and Usage
# The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.

# Syntax
# issubclass(object, subclass)

# Parameter Values
# Parameter	                    Description
# object	                    Required. An object.
# subclass	                    A class object, or a tuple of class objects

# Related Pages
# The isinstance() function, to check if an object is of a certain type.


