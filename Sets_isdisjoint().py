# Python Set isdisjoint() Method

# Example
# Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

# Definition and Usage
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

# Syntax
# set.isdisjoint(set)

# Parameter Values
# Parameter	                Description
# set	                    Required. The set to search for equal items in

# More Examples
# Example

# What if no items are present in both sets?

# Return False if one ore more items are present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

print(z)
