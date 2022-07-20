# Python String center() Method

# Example

# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"

x = txt.center(20)

print(x)

# Definition and Usage

# The center() method will center align the string, using a specified character (space is default) as the fill character.
# Syntax

# string.center(length, character)

# Parameter Values
# Parameter 	Description
# length 	    Required. The length of the returned string
# character 	Optional. The character to fill the missing space on each side. Default is " " (space)

#More Examples
# Example

# Using the letter "O" as the padding character:
txt = "banana"

x = txt.center(20, "O")

print(x)