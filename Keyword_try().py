# Python try Keyword

# Example
# Try a block of code, and decide what to to if it raises an error:
x = 5

try:
  x > 3
except:
  print("Something went wrong")

# Definition and Usage
# The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors.
# You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples below.

# More Examples
# Example
# Raise an error and stop the program when there is an error in the try block:

try:
  x > 3
except:
  Exception("Something went wrong")

# Related Pages
# The except keyword.
# The finally keyword.


