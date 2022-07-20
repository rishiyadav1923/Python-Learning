# Python Strings
# Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
# Example
print("Hello")
print('Hello')
# Assign String to a Variable

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
# Example
z = "Hello"
print(z)

# Multiline Strings

# You can assign a multiline string to a variable by using three quotes:
# Example

# You can use three double quotes:
a = """
    This World is filled with quality & you must protect it at no matter cost.
    """
print(a)

# Or three single quotes:
# Example
c = '''
    This World is filled with quality & you must protect it at no matter cost.
    '''
print(c)

# Note: in the result, the line breaks are inserted at the same position as in the code.
# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.
# Example

# Get the character at position 1 (remember that the first character has the position 0):
d = "Hello, World!"
print(d[1])

# Looping Through a String

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# Learn more about For Loops in our Python For Loops chapter.

# String Length

# To get the length of a string, use the len() function.
# Example

# The len() function returns the length of a string:
e = "Hello, World!"
print(len(e))

# Check String

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Example

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
# Example

# Print only if "free" is present:
text = "The best things in life are free!"
if "free" in text:
  print("Yes, 'free' is present.")

# Learn more about If statements in our Python If...Else chapter.
# Check if NOT

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Example

# Check if "expensive" is NOT present in the following text:
texts = "The best things in life are free!"
print("expensive" not in texts)

# Use it in an if statement:
# Example

# print only if "expensive" is NOT present:
f = "The best things in life are free!"
if "expensive" not in f:
  print("No, 'expensive' is NOT present.")

# Python has a set of built-in methods that you can use on strings.

# *Note: All string methods returns new values. They do not change the original string.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# *Note: All string methods returns new values. They do not change the original string.

