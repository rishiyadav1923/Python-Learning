# Python File tell() Method

# Example
# Find the current file position:

f = open("demofile.txt", "r")
print(f.tell())

# Definition and Usage
# The tell() method returns the current file position in a file stream.

# *Tip: You can change the current file position with the seek() method.

# Syntax
# file.tell()

# Parameter Values
# No parameter values.

# More examples
# Example
# Return the current file position after reading the first line:

f = open("demofile.txt", "r")
print(f.readline())
print(f.tell())

