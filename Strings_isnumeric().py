# Python String isnumeric() Method

# Example
# Check if all the characters in the text are numeric:

txt = "565543"

x = txt.isnumeric()

print(x)

# Definition and Usage
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

# Exponents, like ² and ¾ are also considered to be numeric values.

# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

# Syntax
# string.isnumeric()

# Parameter Values
# No parameters.

# More Examples
# Example
# Check if the characters are numeric:

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
