# Python dir() Function

# Example
# Display the content of an object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

# Definition and Usage
# The dir() function returns all properties and methods of the specified object, without the values.

# This function will return all the properties and methods, even built-in properties which are default for all object.

# Syntax
# dir(object)

# Parameter Values
# Parameter	                Description
# object	                The object you want to see the valid attributes of

