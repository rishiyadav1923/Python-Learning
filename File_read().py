# Python File read() Method

# Example
# Read the content of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.read())

# Definition and Usage
# The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.

# Syntax
# file.read()

# Parameter Values
# Parameter	            Description
# size	                Optional. The number of bytes to return. Default -1, which means the whole file.

# More examples
# Example
# Read the content of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.read(33))

