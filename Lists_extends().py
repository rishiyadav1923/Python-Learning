# Python List extend() Method

# Example
# Add the elements of cars to the fruits list:

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

# Definition and Usage
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.

# Syntax
# list.extend(iterable)

# Parameter Values
# Parameter	            Description
# iterable	            Required. Any iterable (list, set, tuple, etc.)

# More Examples
# Example
# Add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

