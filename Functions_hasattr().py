# Python hasattr() Function

# Example
# Check if the "Person" object has the "age" property:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')

# Definition and Usage
# The hasattr() function returns True if the specified object has the specified attribute, otherwise False.

# Syntax
# hasattr(object, attribute)

# Parameter Values
# Parameter	                                Description
# object	                                Required. An object.
# attribute	                                The name of the attribute you want to check if exists

# Related Pages
# The delattr() function, to remove an attribute
# The getattr() function, to get the value of an attribute
# The setattr() function, to set the value of an attribute


