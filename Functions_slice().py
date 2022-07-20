# Python slice() Function

# Example
# Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

# Definition and Usage
# The slice() function returns a slice object.

# A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.

# Syntax
# slice(start, end, step)

# Parameter Values
# Parameter	            Description
# start	                Optional. An integer number specifying at which position to start the slicing. Default is 0
# end	                An integer number specifying at which position to end the slicing
# step	                Optional. An integer number specifying the step of the slicing. Default is 1

# More Examples
# Example
# Create a tuple and a slice object. Start the slice object at position 3, and slice to position 5, and return the result:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

# Example
# Create a tuple and a slice object. Use the step parameter to return every third item:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

