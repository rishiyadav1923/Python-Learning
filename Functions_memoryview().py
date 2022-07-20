# Python memoryview() Function

# Example
# Create and print a memoryview object:

x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])

# Definition and Usage
# The memoryview() function returns a memory view object from a specified object.

# Syntax
# memoryview(obj)

# Parameter Values
# Parameter	                Description
# obj	                    A Bytes object or a Bytearray object.

