# Python - Format - Strings
# String Format

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# Example

"""
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

# But we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Example

# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# Example

quantity = 3
ItemNo = 567
price = 49.95
MyOrder = "I want {} pieces of item {} for {} dollars."
print(MyOrder.format(quantity, ItemNo, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example
Quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myOrder.format(quantity, itemNo, price))
