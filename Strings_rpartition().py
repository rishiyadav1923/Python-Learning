# Python String rpartition() Method

# Example
# Search for the last occurrence of the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

# Definition and Usage
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

# The first element contains the part before the specified string.

# The second element contains the specified string.

# The third element contains the part after the string.

# Syntax
# string.rpartition(value)

# Parameter Values
# Parameter	                Description
# value	                    Required. The string to search for

# More Examples
# Example
# If the specified value is not found, the rpartition() method returns a tuple containing: 1 - an empty string, 2 - an empty string, 3 - the whole string:

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)
