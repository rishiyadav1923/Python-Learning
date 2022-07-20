# Python Set discard() Method

# Example
# Remove "banana" from the set:

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

# Definition and Usage
# The discard() method removes the specified item from the set.

# This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

# Syntax
# set.discard(value)

# Parameter Values
# Parameter	                Description
# value	                    Required. The item to search for, and remove

