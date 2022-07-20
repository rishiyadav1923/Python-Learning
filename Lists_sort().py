# Python List sort() Method

# Example
# Sort the list alphabetically:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

# Definition and Usage
# The sort() method sorts the list ascending by default.

# You can also make a function to decide the sorting criteria(s).

# Syntax
# list.sort(reverse=True|False, key=myFunc)

# Parameter Values
# Parameter	                    Description
# reverse	                    Optional. reverse=True will sort the list descending. Default is reverse=False
# key	                        Optional. A function to specify the sorting criteria(s)

# More Examples
# Example
# Sort the list descending:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

# Example
# Sort the list by the length of the values:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

# Example
# Sort a list of dictionaries based on the "year" value of the dictionaries:

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

# Example
# Sort the list by the length of the values and reversed:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

