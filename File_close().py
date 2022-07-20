# Python File close() Method

# Example
# Close a file after it has been opened:

f = open("demofile.txt", "r")
print(f.read())
f.close()

# Definition and Usage
# The close() method closes an open file.
# You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# Syntax
# file.close()

# Parameter Values
# No parameters


