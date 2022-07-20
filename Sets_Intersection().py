# Python Set intersection() Method

# Example
# Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Definition and Usage
# The intersection() method returns a set that contains the similarity between two or more sets.

# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

# Syntax
# set.intersection(set1, set2 ... etc)

# Parameter Values
# Parameter	                    Description
# set1	                        Required. The set to search for equal items in
# set2	                        Optional. The other set to search for equal items in.

# You can compare as many sets you like.
# Separate the sets with a comma
# More Examples
# Example

# Compare 3 sets, and return a set with items that is present in all 3 sets:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
