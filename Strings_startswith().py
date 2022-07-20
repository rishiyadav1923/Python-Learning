# Python String startswith() Method

# Example
# Check if the string starts with "Hello":

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

# Definition and Usage
# The startswith() method returns True if the string starts with the specified value, otherwise False.

# Syntax
# string.startswith(value, start, end)

# Parameter Values
# Parameter	                    Description
# value	                        Required. The value to check if the string starts with
# start	                        Optional. An Integer specifying at which position to start the search
# end                           Optional. An Integer specifying at which position to end the search

# More Examples
# Example
# Check if position 7 to 20 starts with the characters "wel":

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)

