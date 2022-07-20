# Python Dictionary values() Method

# Example
# Return the values:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

# Definition and Usage
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.

# The view object will reflect any changes done to the dictionary, see example below.

# Syntax
# dictionary.values()

# Parameter Values
# No parameters

# More Examples
# Example
# When a values is changed in the dictionary, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)

