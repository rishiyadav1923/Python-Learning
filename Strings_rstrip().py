# Python String rstrip() Method

# Example
# Remove any white spaces at the end of the string:

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

# Definition and Usage
# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

# Syntax
# string.rstrip(characters)

# Parameter Values
# Parameter	                Description
# characters	                Optional. A set of characters to remove as trailing characters

# More Examples
# Example
# Remove the trailing characters if they are commas, s, q, or w:

txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)

