# Python vars() Function

# Example
# Return the __dict__ attribute of an object called Person:

class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)

# Definition and Usage
# The vars() function returns the __dic__ attribute of an object.
# The __dict__ attribute is a dictionary containing the object's changeable attributes.

# *Note: calling the vars() function without parameters will return a dictionary containing the local symbol table.

# Syntax
# vars(object)

# Parameter Values
# Parameter	            Description
# object	            Any object with a __dict__attribute

