# Python String format() Method

# Example
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# Definition and Usage
# The format() method formats the specified value(s) and insert them inside the string's placeholder.

# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

# The format() method returns the formatted string.

# Syntax
# string.format(value1, value2...)

# Parameter Values
# Parameter	                Description
# value1, value2...	        Required. One or more values that should be formatted and inserted in the string.

# The values are either a list of values separated by commas, a key=value list, or a combination of both.

# The values can be of any data type.
# The Placeholders
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

# Example
# Using different placeholder values:

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

# Formatting Types

# Inside the placeholders you can add a formatting type to format the result:

# :< ->	Left aligns the result (within the available space)
txt4 = "We have {:<8} chickens."
print(txt4.format(49))

# :> -> Right aligns the result (within the available space)
txt5 = "We have {:>8} chickens."
print(txt5.format(49))

# :^ ->	Center aligns the result (within the available space)
txt6 = "We have {:^8} chickens."
print(txt6.format(49))

# := ->	Places the sign to the left most position
txt7 = "The temperature is {:=8} degrees celsius."
print(txt7.format(-5))

# :+ ->	Use a plus sign to indicate if the result is positive or negative
txt8 = "The temperature is between {:+} and {:+} degrees celsius."
print(txt8.format(-3, 7))

# :- -> Use a minus sign for negative values only
txt9 = "The temperature is between {:-} and {:-} degrees celsius."
print(txt9.format(-3, 7))

# : ->  Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
txt10 = "The temperature is between {: } and {: } degrees celsius."
print(txt10.format(-3, 7))

# :, ->	Use a comma as a thousand separator
txt11 = "The universe is {:,} years old."
print(txt11.format(13800000000))

# :_ ->	Use a underscore as a thousand separator
txt12 = "The universe is {:_} years old."
print(txt12.format(13800000000))

# :b ->	Binary format
txt13 = "The binary version of {0} is {0:b}"
print(txt13.format(5))

# :c ->	Converts the value into the corresponding unicode character
txt14 = "The corresponding unicode value of {0} is {0:c}"
print(txt14.format(3209504))

# :d ->	Decimal format
txt15 = "We have {:d} chickens."
print(txt15.format(0b101))

# :e ->	Scientific format, with a lower case e
txt16 = "We have {:e} chickens."
print(txt16.format(5))

# :E ->	Scientific format, with an upper case E
txt17 = "We have {:E} chickens."
print(txt17.format(5))

# :f ->	Fix point number format
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt18 = "The price is {:.2f} dollars."
print(txt18.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt19 = "The price is {:f} dollars."
print(txt19.format(45))


# :F ->	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt20 = "The price is {:F} dollars."
print(txt20.format(x))

#same example, but with a lower case f:

txt21 = "The price is {:f} dollars."
print(txt21.format(x))

# :g ->	General format


# :G ->	General format (using a upper case E for scientific notations)


# :o ->	Octal format
txt22 = "The octal version of {0} is {0:o}"
print(txt22.format(10))

# :x ->	Hex format, lower case
txt23 = "The Hexadecimal version of {0} is {0:x}"
print(txt23.format(255))

# :X ->	Hex format, upper case
txt24 = "The Hexadecimal version of {0} is {0:X}"
print(txt24.format(255))

# :n ->	Number format


# :% -> Percentage format
txt25 = "You scored {:%}"
print(txt25.format(0.25))

#Or, without any decimals:

txt26 = "You scored {:.0%}"
print(txt26.format(0.25))


