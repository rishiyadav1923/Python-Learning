# Python String isdigit() Method

# Example
# Check if all the characters in the text are digits:

txt = "50800"

x = txt.isdigit()

print(x)

# Definition and Usage
# The isdigit() method returns True if all the characters are digits, otherwise False.

# Exponents, like ², are also considered to be a digit.

# Syntax
# string.isdigit()
# Parameter Values
# No parameters.

# More Examples
# Example
# Check if all the characters in the text are digits:

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())