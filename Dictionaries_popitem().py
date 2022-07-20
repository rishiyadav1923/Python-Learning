# Python Dictionary popitem() Method

# Example
# Remove the last item from the dictionary:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

# Definition and Usage
# The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.

# The removed item is the return value of the popitem() method, as a tuple, see example below.

# Syntax
# dictionary.popitem()

# Parameter Values
# No parameters

# More Examples
# Example
# The removed item is the return value of the pop() method:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)