# Python Set symmetric_difference_update() Method

# Example
# Remove the items that are present in both sets, AND insert the items that is not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# Definition and Usage
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.

# Syntax
# set.symmetric_difference_update(set)

# Parameter Values
# Parameter	                    Description
# set	                        Required. The set to check for matches in

