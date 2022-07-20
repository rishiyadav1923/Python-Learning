# Python format() Function

# Example
# Format the number 0.5 into a percentage value:

x = format(0.5, '%')

# Definition and Usage
# The format() function formats a specified value into a specified format.

# Syntax
# format(value, format)

# Parameter Values
# Parameter	                    Description
# value	                        A value of any format
# format	                    The format you want to format the value into.

# Legal values:

"""
'<' - Left aligns the result (within the available space)
'>' - Right aligns the result (within the available space)
'^' - Center aligns the result (within the available space)
'=' - Places the sign to the left most position
'+' - Use a plus sign to indicate if the result is positive or negative
'-' - Use a minus sign for negative values only
' ' - Use a leading space for positive numbers
',' - Use a comma as a thousand separator
'_' - Use a underscore as a thousand separator
'b' - Binary format
'c' - Converts the value into the corresponding unicode character
'd' - Decimal format
'e' - Scientific format, with a lower case e
'E' - Scientific format, with an upper case E
'f' - Fix point number format
'F' - Fix point number format, upper case
'g' - General format
'G' - General format (using a upper case E for scientific notations)
'o' - Octal format
'x' - Hex format, lower case
'X' - Hex format, upper case
'n' - Number format
'%' - Percentage format

    """

# More Examples
# Example
# Format 255 into a hexadecimal value:

x = format(255, 'x')
