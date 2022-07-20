# Python Dictionary setdefault() Method

# Example
# Get the value of the "model" item:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

# Definition and Usage
# The setdefault() method returns the value of the item with the specified key.

# If the key does not exist, insert the key, with the specified value, see example below

# Syntax
# dictionary.setdefault(keyname, value)

# Parameter Values
# Parameter	                            Description
# keyname	                            Required. The keyname of the item you want to return the value from

# value	                                Optional. If the key exist, this parameter has no effect.
#                                       If the key does not exist, this value becomes the key's value
#                                       Default value None

# More Examples
# Example
# Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)

