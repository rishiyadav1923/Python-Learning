# Python String isprintable() Method

# Example
# Check if all the characters in the text are printable:

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

# Definition and Usage
# The isprintable() method returns True if all the characters are printable, otherwise False.

# Example of none printable character can be carriage return and line feed.

# Syntax
# string.isprintable()

# Parameter Values
# No parameters.

# More Examples
# Example
# Check if all the characters in the text are printable:

txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)