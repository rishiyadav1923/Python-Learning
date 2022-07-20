# Python File readline() Method

# Example
# Read the first line of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.readline())

# Definition and Usage
# The readline() method returns one line from the file.
# You can also specified how many bytes from the line to return, by using the size parameter.

# Syntax
# file.readline(size)

# Parameter Values
# Parameter	            Description
# size	                Optional. The number of bytes from the line to return. Default -1, which means the whole line.

# More examples
# Example
# Call readline() twice to return both the first and the second line:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Example
# Return only the five first bytes from the first line:

f = open("demofile.txt", "r")
print(f.readline(5))

