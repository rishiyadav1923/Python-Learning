# Python - Modify Strings

# Python has a set of built-in methods that you can use on strings.
# Upper Case
# Example

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# Lower Case
# Example

# The lower() method returns the string in lower case:
b = "Hello, World!"
print(b.lower())

# Remove Whitespace

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# Example

# The strip() method removes any whitespace from the beginning or the end:
c = " Hello, World! "
print(c.strip()) # returns "Hello, World!"

# Replace String
# Example

# The replace() method replaces a string with another string:
d = "Hello, World!"
print(d.replace("H", "J"))

# Split String

# The split() method returns a list where the text between the specified separator becomes the list items.
# Example

# The split() method splits the string into substrings if it finds instances of the separator:
e = "Hello, World!"
print(e.split(",")) # returns ['Hello', ' World!']