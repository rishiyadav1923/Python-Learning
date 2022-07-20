# Python else Keyword

# Example
# Print "YES" if x larger than 3, otherwise print "NO":

x = 2
if x > 3:
  print("YES")
else:
  print("NO")
# Definition and Usage
# The else keyword is used in conditional statements (if statements), and decides what to do if the condition is False.
# The else keyword can also be use in try...except blocks, see example below.

# More Examples
# Example
# Use the else keyword in a try...except block to define what to do if no errors were raised:

x = 5

try:
  x > 10
except:
  print("Something went wrong")
else:
  print("The 'Try' code was executed without raising any errors!")

# Related Pages
# The if keyword.
# The elif keyword.
# Read more about conditional statements in our Python Conditions Tutorial.


