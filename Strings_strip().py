# Python String strip() Method

# Example
# Remove spaces at the beginning and at the end of the string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

# Definition and Usage
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

# Syntax
# string.strip(characters)

# Parameter Values
# Parameter	                    Description
# characters	                Optional. A set of characters to remove as leading/trailing characters

# More Examples
# Example
# Remove the leading and trailing characters:

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
