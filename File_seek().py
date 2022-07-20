# Python File seek() Method

# Example
# Change the current file position to 4, and return the rest of the line:

f = open("demofile.txt", "r")
f.seek(4)
print(f.readline())

# Definition and Usage
# The seek() method sets the current file position in a file stream.
# The seek() method also returns the new postion.

# Syntax
# file.seek(offset)

# Parameter Values
# Parameter	Description
# offset	Required. A number representing the position to set the current file stream position.

# More examples
# Example
# Return the new position:

f = open("demofile.txt", "r")
print(f.seek(4))

