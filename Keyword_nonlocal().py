# Python nonlocal Keyword

# Example
# Make a function inside a function, which uses the variable x as a non local variable:

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# Definition and Usage
# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# Use the keyword nonlocal to declare that the variable is not local.

# More Examples
# Example
# Same example as above, but without the nonlocal keyword:

def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# Related Pages
# The keyword global is used to make global variables.


