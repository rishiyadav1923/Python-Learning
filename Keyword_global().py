# Python global Keyword

# Example
# Declare a global variable inside a function, and use it outside the function:

#create a function:
def myfunction():
  global x
  x = "hello"

#execute the function:
myfunction()

#x should now be global, and accessible in the global scope.
print(x)

# Definition and Usage
# The global keyword is used to create global variables from a no-global scope, e.g. inside a function.


