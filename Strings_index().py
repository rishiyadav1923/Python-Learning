# Python String index() Method

# Example
# Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

# Definition and Usage
# The index() method finds the first occurrence of the specified value.

# The index() method raises an exception if the value is not found.

# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)

# Syntax
# string.index(value, start, end)

# Parameter Values
# Parameter	            Description
# value	                Required. The value to search for
# start	                Optional. Where to start the search. Default is 0
# end	                    Optional. Where to end the search. Default is to the end of the string

# More Examples
# Example
# Where in the text is the first occurrence of the letter "e"?:

txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)

# Example
# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)

# Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:

txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))
