# Python Set difference_update() Method

# Example
# Remove the items that exist in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

# Definition and Usage
# The difference_update() method removes the items that exist in both sets.

# The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

# Syntax
# set.difference_update(set)

# Parameter Values
# Parameter	                Description
# set	                    Required. The set to check for differences in

