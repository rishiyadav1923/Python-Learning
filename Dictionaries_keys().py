# Python Dictionary keys() Method

# Example
# Return the keys:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

# Definition and Usage
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

# The view object will reflect any changes done to the dictionary, see example below.

# Syntax
# dictionary.keys()

# Parameter Values
# No parameters

# More Examples
# Example
# When an item is added in the dictionary, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)
