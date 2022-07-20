# Python Set union() Method

# Example
# Return a set that contains all items from both sets, duplicates are excluded:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

# Definition and Usage
# The union() method returns a set that contains all items from the original set, and all items from the specified set(s).

# You can specify as many sets you want, separated by commas.

# It does not have to be a set, it can be any iterable object.

# If an item is present in more than one set, the result will contain only one appearance of this item.

# Syntax
# set.union(set1, set2...)

# Parameter Values
# Parameter	                    Description
# set1	                        Required. The iterable to unify with
# set2	                        Optional. The other iterable to unify with.

# You can compare as many iterables as you like.
# Separate each iterable with a comma

# More Examples
# Example
# Unify more than 2 sets:

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)

