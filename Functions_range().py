# Python range() Function

# Example
# Create a sequence of numbers from 0 to 5, and print each item in the sequence:

x = range(6)
for n in x:
  print(n)

# Definition and Usage
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# Syntax
# range(start, stop, step)

# Parameter Values
# Parameter	                    Description
# start	                        Optional. An integer number specifying at which position to start. Default is 0
# stop	                        Required. An integer number specifying at which position to stop (not included).
# step	                        Optional. An integer number specifying the incrementation. Default is 1

# More Examples
# Example
# Create a sequence of numbers from 3 to 5, and print each item in the sequence:

x = range(3, 6)
for n in x:
  print(n)

# Example
# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:

x = range(3, 20, 2)
for n in x:
  print(n)

