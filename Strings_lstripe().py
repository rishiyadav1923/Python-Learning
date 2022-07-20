# Python String lstrip() Method

# Example
# Remove spaces to the left of the string:

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

# Definition and Usage
# The lstrip() method removes any leading characters (space is the default leading character to remove)

# Syntax
# string.lstrip(characters)

# Parameter Values
# Parameter	            Description
# characters	        Optional. A set of characters to remove as leading characters

# More Examples
# Example
# Remove the leading characters:

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
