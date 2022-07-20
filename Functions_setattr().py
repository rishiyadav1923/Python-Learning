# Python setattr() Function

# Example
# Change the value of the "age" property of the "person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

# Definition and Usage
# The setattr() function sets the value of the specified attribute of the specified object.

# Syntax
# setattr(object, attribute, value)

# Parameter Values
# Parameter	                Description
# object	                Required. An object.
# attribute	                Required. The name of the attribute you want to set
# value	                    Required. The value you want to give the specified attribute

# Related Pages
# The delattr() function, to remove an attribute
# The getattr() function, to get the value of an attribute
# The hasattr() function, to check if an attribute exist


