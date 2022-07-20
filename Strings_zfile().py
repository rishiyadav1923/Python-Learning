# Python String zfill() Method

# Example
# Fill the string with zeros until it is 10 characters long:

txt = "50"

x = txt.zfill(10)

print(x)

# Definition and Usage
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

# If the value of the len parameter is less than the length of the string, no filling is done.

# Syntax
# string.zfill(len)
# Parameter Values
# Parameter	                    Description
# len	                        Required. A number specifying the desired length of the string

# More Examples
# Example
# Fill the strings with zeros until they are 10 characters long:

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

