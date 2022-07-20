# Python Set symmetric_difference() Method

# Example
# Return a set that contains all items from both sets, except items that are present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# Definition and Usage
# The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

# Meaning: The returned set contains a mix of items that are not present in both sets.

# Syntax
# set.symmetric_difference(set)

# Parameter Values
# Parameter	                    Description
# set	                        Required. The set to check for matches in

