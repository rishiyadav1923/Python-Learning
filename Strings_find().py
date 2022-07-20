# Python String find() Method

# Example
# Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

# Definition and Usage

# The find() method finds the first occurrence of the specified value.

# The find() method returns -1 if the value is not found.

# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

# Syntax
# string.find(value, start, end)
# Parameter Values
# Parameter	                Description
# value	                    Required. The value to search for
# start	                    Optional. Where to start the search. Default is 0
# end	                    Optional. Where to end the search. Default is to the end of the string

# More Examples
# Example
# Where in the text is the first occurrence of the letter "e"?:

txt1 = "Hello, welcome to my world."

x1 = txt1.find("e")

print(x1)

# Example
# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:

txt2 = "Hello, welcome to my world."

x2 = txt2.find("e", 5, 10)

print(x2)

# Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:

txt3 = "Hello, welcome to my world."

print(txt3.find("q"))
print(txt3.index("q"))
