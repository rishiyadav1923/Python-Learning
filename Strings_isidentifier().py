# Python String isidentifier() Method

# Example
# Check if the string is a valid identifier:

txt = "Demo"

x = txt.isidentifier()

print(x)

# Definition and Usage
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.

# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

# Syntax
# string.isidentifier()
# Parameter Values
# No parameters.

# More Examples
# Example
# Check if the strings are valid identifiers:

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
