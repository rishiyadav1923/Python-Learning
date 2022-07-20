# Python Dictionary pop() Method

# Example
# Remove "model" from the dictionary:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

# Definition and Usage
# The pop() method removes the specified item from the dictionary.

# The value of the removed item is the return value of the pop() method, see example below.

# Syntax
# dictionary.pop(keyname, defaultvalue)

# Parameter Values
# Parameter	                            Description
# keyname	                            Required. The keyname of the item you want to remove
# defaultvalue	                        Optional. A value to return if the specified key do not exist.

# If this parameter is not specified, and the no item with the specified key is found, an error is raised
# More Examples
# Example
# The value of the removed item is the return value of the pop() method:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)

