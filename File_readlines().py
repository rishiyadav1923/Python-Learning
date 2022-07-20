# Python File readlines() Method

# Example
# Return all lines in the file, as a list where each line is an item in the list object:

f = open("demofile.txt", "r")
print(f.readlines())

# Definition and Usage
# The readlines() method returns a list containing each line in the file as a list item.
# Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the specified number, no more lines are returned.

# Syntax
# file.readlines(hint)

# Parameter Values
# Parameter	        Description
# hint	            Optional. If the number of bytes returned exceed the hint number, no more lines will be returned. Default value is  -1, which means all lines will be returned.

# More examples
# Example
# Do not return the next line if the total number of returned bytes are more than 33:

f = open("demofile.txt", "r")
print(f.readlines(33))

