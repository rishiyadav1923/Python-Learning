# Python String encode() Method

# Example
# UTF-8 encode the string:

txt = "My name is Stale"

x = txt.encode()

print(x)

# Definition and Usage
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

# Syntax
# string.encode(encoding=encoding, errors=errors)

#Parameter Values
# Parameter	          Description
# encoding	          Optional. A String specifying the encoding to use. Default is UTF-8
# errors             	  Optional. A String specifying the error method. Legal values are:
#                      'backslashreplace'	- uses a backslash instead of the character that could not be encoded
#                      'ignore'	- ignores the characters that cannot be encoded
#                      'namereplace'	- replaces the character with a text explaining the character
#                      'strict'	- Default, raises an error on failure
#                      'replace'	- replaces the character with a questionmark
#                      'xmlcharrefreplace'	- replaces the character with an xml character

# More Examples
# Example
# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:

txt = "My name is Stale"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
