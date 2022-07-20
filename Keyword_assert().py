# Python assert Keyword

# Example
# Test if a condition returns True:

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"

# Definition and Usage
# The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
# You can write a message to be written if the code returns False, check the example below.

# More Examples
# Example
# Write a message if the condition is False:

x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"

