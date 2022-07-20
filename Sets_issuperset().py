# Python Set issuperset() Method

# Example
# Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

# Definition and Usage
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.

# Syntax
# set.issuperset(set)
# Parameter Values
# Parameter	                        Description
# set	                            Required. The set to search for equal items in

# More Examples
# Example
# What if not all items are present in the specified set?

# Return False if not all items in set y are present in set x:

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
