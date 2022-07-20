# Python exec() Function

# Example
# Execute a block of code:

x = 'name = "John"\nprint(name)'
exec(x)

# Definition and Usage
# The exec() function executes the specified Python code.

# The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression

# Syntax
# exec(object, globals, locals)

# Parameter Values
# Parameter	            Description
# object	            A String, or a code object
# globals	            Optional. A dictionary containing global parameters
# locals	            Optional. A dictionary containing local parameters

