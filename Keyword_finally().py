# Python finally Keyword

# Example
# The finally block will always be executed, no matter if the try block raises an error or not:
x = 5

try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")

# Definition and Usage
# The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final.
# The finally block will be executed no matter if the try block raises an error or not.
# This can be useful to close objects and clean up resources.

# Related Pages
# The try keyword.

# The except keyword.


