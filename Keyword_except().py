# Python except Keyword

# Example
# If the statement raises an error print "Something went wrong":
x = 5

try:
  x > 3
except:
  print("Something went wrong")

# Definition and Usage
# The except keyword is used in try...except blocks. It defines a block of code to run if the try block raises an error.
# You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples below.

# More Examples
# Example
# Write one message if it is a NameError, and another if it is an TypeError:

x = "hello"

try:
  x > 3
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")

# Example
# Try to execute a statement that raises an error, but none of the defined error types (in this case, a ZeroDivisionError):

try:
  x = 1/0
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
except:
  print("Something else went wrong")

# Example
# Write a message if no errors were raised:

x = 1

try:
  x > 10
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
else:
  print("The 'Try' code was executed without raising any errors!")

# Related Pages
# The try keyword.
# The finally keyword.


