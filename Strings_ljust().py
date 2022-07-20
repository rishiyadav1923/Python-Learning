# Python String ljust() Method

# Example
# Return a 20 characters long, left justified version of the word "banana":

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

# Note: In the result, there are actually 14 whitespaces to the right of the word banana.

# Definition and Usage
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.

# Syntax
# string.ljust(length, character)

# Parameter Values
# Parameter	                Description
# length	                Required. The length of the returned string
# character	Optional. A character to fill the missing space (to the right of the string). Default is " " (space).

# More Examples
# Example
# Using the letter "O" as the padding character:

txt = "banana"

x = txt.ljust(20, "O")

print(x)

