# Python isinstance() Function

# Example
# Check if the number 5 is an integer:

x = isinstance(5, int)

# Definition and Usage
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

# Syntax
# isinstance(object, type)

# Parameter Values
# Parameter	                Description
# object	                Required. An object.
# type	                    A type or a class, or a tuple of types and/or classes

# More Examples
# Example
# Check if "Hello" is one of the types described in the type parameter:

x = isinstance("Hello", (float, int, str, list, dict, tuple))

# Example
# Check if y is an instance of myObj:

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)

# Related Pages
# The issubclass() function, to check if an object is a subclass of another object.


