# Python - Escape Characters
# Escape Character

# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# Example

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

"""
txt = "We are the so-called "Vikings" from the north."
"""

# To fix this problem, use the escape character \":
# Example

# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Characters

# Other escape characters used in Python:


# \' 	Single Quote
# \\ 	Backslash
# \n 	New Line
# \r 	Carriage Return
# \t 	Tab
# \b 	Backspace
# \f 	Form Feed
# \ooo 	Octal value
# \xhh 	Hex value


txt1 = "We are the so-called \'Vikings\' from the north."
print(txt1)

txt2 = "We are the so-called \\Vikings\\ from the north."
print(txt2)

txt3 = "We are the so-called \nVikings\n from the north."
print(txt3)

txt4 = "We are the so-called \rVikings\r from the north."
print(txt4)

txt5 = "We are the so-called \tVikings\t from the north."
print(txt5)

txt6 = "We are the so-called \bVikings\b from the north."
print(txt6)

txt7 = "We are the so-called \fVikings\f from the north."
print(txt7)

txt8 = "We are the so-called \000Vikings\000 from the north."
print(txt8)

# Used to find hex value
# txt9 = "We are the so-called \xhhVikings\xhh from the north."
