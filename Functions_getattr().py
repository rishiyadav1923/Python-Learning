# Python getattr() Function

# Example
# Get the value of the "age" property of the "Person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')

# Definition and Usage
# The getattr() function returns the value of the specified attribute from the specified object.

# Syntax
# getattr(object, attribute, default)

# Parameter Values
# Parameter	                Description
# object	                Required. An object.
# attribute	                The name of the attribute you want to get the value from
# default	                Optional. The value to return if the attribute does not exist

# More Examples
# Example
# Use the "default" parameter to write a message when the attribute does not exist:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')

# Related Pages
# The delattr() function, to remove an attribute
# The hasattr() function, to check if an attribute exist
# The setattr() function, to set the value of an attribute


