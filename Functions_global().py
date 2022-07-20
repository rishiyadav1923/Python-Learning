# Python globals() Function

# Example
# Display the global symbol table:

x = globals()
print(x)

# Definition and Usage
# The globals() function returns the global symbol table as a dictionary.

# A symbol table contains necessary information about the current program

# Syntax
# globals()

# Parameter Values
# No parameters

# More Examples
# Example

# Get the filename of the current program:

x = globals()
print(x["__file__"])

