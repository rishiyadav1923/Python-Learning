# Python File truncate() Method

# Example
# Open the file with "a" for appending, then truncate the file to 20 bytes:

f = open("demofile2.txt", "a")
f.truncate(20)
f.close()

#open and read the file after the truncate:
f = open("demofile2.txt", "r")
print(f.read())

# Definition and Usage
# The truncate() method resizes the file to the given number of bytes.
# If the size is not specified, the current position will be used.

# Syntax
# file.truncate(size)

# Parameter Values
# Parameter	            Description
# size	                Optional. The size of the file (in bytes) after the truncate. Default None, which means the current file stream position.

