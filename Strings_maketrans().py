# Python String maketrans() Method

# Example
# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# Definition and Usage
# The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.

# Syntax
# string.maketrans(x, y, z)
# Parameter Values
# Parameter	                    Description
# x	                            Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
# y	                            Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
# z	                            Optional. A string describing which characters to remove from the original string.

# More Examples
# Example
# Use a mapping table to replace many characters:

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

# Example
# The third parameter in the mapping table describes characters that you want to remove from the string:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))

# Example
# The maketrans() method itself returns a dictionary describing each replacement, in unicode:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
