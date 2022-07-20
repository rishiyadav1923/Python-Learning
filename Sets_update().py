# Python Set update() Method

# Example
# Insert the items from set y into set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)

# Definition and Usage
# The update() method updates the current set, by adding items from another set (or any other iterable).

# If an item is present in both sets, only one appearance of this item will be present in the updated set.

# Syntax
# set.update(set)

# Parameter Values
# Parameter	                    Description
# set	                        Required. The iterable insert into the current set

