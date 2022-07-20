# Python Set difference() Method

# Example
# Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

# Definition and Usage
# The difference() method returns a set that contains the difference between two sets.

# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

# Syntax
# set.difference(set)

# Parameter Values
# Parameter	                Description
# set	                    Required. The set to check for differences in

# More Examples
# Example
# Reverse the first example. Return a set that contains the items that only exist in set y, and not in set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z)

