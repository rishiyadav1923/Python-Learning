# Python String translate() Method

# Example
# Replace any "S" characters with a "P" character:

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# Definition and Usage
# The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

# Use the maketrans() method to create a mapping table.

# If a character is not specified in the dictionary/table, the character will not be replaced.

# If you use a dictionary, you must use ascii codes instead of characters.

# Syntax
# string.translate(table)
# Parameter Values
# Parameter	Description
# table	Required. Either a dictionary, or a mapping table describing how to perform the replace
# More Examples
# Example
# Use a mapping table to replace "S" with "P":

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

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
# The same example as above, but using a dictionary instead of a mapping table:

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

