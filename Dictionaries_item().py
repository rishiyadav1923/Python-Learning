# Python Dictionary items() Method

# Example
# Return the dictionary's key-value pairs:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

# Definition and Usage
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

# The view object will reflect any changes done to the dictionary, see example below.

# Syntax
# dictionary.items()

# Parameter Values
# No parameters

# More Examples
# Example
# When an item in the dictionary changes value, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)

