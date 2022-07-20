# Python delattr() Function

# Example
# Delete the "age" property from the "person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')

# Definition and Usage
# The delattr() function will delete the specified attribute from the specified object.

# Syntax
# delattr(object, attribute)

# Parameter Values
# Parameter	                  Description
# object	                    Required. An object.
# attribute	                  Required. The name of the attribute you want to remove

# Related Pages
# The getattr() function, to get the value of an attribute
# The hasattr() function, to check if an attribute exist
# The setattr() function, to set the value of an attribute


