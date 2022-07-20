# Python String casefold() Method

# Example

# Make the string lower case:
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

# Definition and Usage

# The casefold() method returns a string where all the characters are lower case.

# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
# Syntax

import string

string.casefold()
# Parameter Values

# No parameters