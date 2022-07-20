# Python String splitlines() Method

# Example
# Split a string into a list where each line is a list item:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

# Definition and Usage
# The splitlines() method splits a string into a list. The splitting is done at line breaks.

# Syntax
# string.splitlines(keeplinebreaks)

# Parameter Values
# Parameter	                Description
# keeplinebreaks	            Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False

# More Examples
# Example
# Split the string, but keep the line breaks:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)

