# Python String isdecimal() Method

# Example
# Check if all the characters in the unicode object are decimals:

txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

# Definition and Usage
# The isdecimal() method returns True if all the characters are decimals (0-9).

# This method is used on unicode objects.

# Syntax
# string.isdecimal()

# Parameter Values
# No parameters.

# More Examples
# Example
#Check if all the characters in the unicode are decimals:

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())