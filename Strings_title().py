# Python String title() Method

# Example
# Make the first letter in each word upper case:

txt = "Welcome to my world"

x = txt.title()

print(x)

# Definition and Usage
# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

# If the word contains a number or a symbol, the first letter after that will be converted to upper case.

# Syntax
# string.title()

# Parameter Values
# No parameters.

# More Examples
# Example
# Make the first letter in each word upper case:

txt = "Welcome to my 2nd world"

x = txt.title()

print(x)

# Example
# Note that the first letter after a non-alphabet letter is converted into a upper case letter:

txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)

