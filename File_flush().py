# Python File flush() Method

# Example
# You can clear the buffer when writing to a file:

f = open("myfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

# Definition and Usage
# The flush() method cleans out the internal buffer.

# Syntax
# file.flush()

# Parameter Values
# No parameters


