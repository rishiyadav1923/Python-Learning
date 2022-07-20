# Python locals() Function

# Example
# Display the local symbol table:

x = locals()
print(x)

# Definition and Usage
# The locals() function returns the local symbol table as a dictionary.

# A symbol table contains necessary information about the current program.

# Syntax
# locals()

# Parameter Values
# No parameters

# More Examples
# Example

# Get the filename of the current program:

x = locals()
print(x["__file__"])

