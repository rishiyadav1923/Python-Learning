# Python Set issubset() Method

# Example
# Return True if all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

# Definition and Usage
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.

# Syntax
# set.issubset(set)

# Parameter Values
# Parameter	                    Description
# set	                        Required. The set to search for equal items in

# More Examples
# Example
# What if not all items are present in the specified set?

# Return False if not all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)
