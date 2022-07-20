# Python String partition() Method

# Example
# Search for the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

# Definition and Usage
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

# The first element contains the part before the specified string.

# The second element contains the specified string.

# The third element contains the part after the string.

# Note: This method searches for the first occurrence of the specified string.

# Syntax
# string.partition(value)

# Parameter Values
# Parameter	                Description
# value	                    Required. The string to search for

# More Examples
# Example
# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)
