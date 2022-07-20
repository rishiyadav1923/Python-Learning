# Python Set intersection_update() Method

# Example
# Remove the items that is not present in both x and y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Definition and Usage
# The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).

# The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.

# Syntax
# set.intersection_update(set1, set2 ... etc)

# Parameter Values
# Parameter	                Description
# set1	                    Required. The set to search for equal items in
# set2	                    Optional. The other set to search for equal items in.

# You can compare as many sets you like.
# Separate the sets with a comma

# More Examples
# Example
# Compare 3 sets, and return a set with items that is present in all 3 sets:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
