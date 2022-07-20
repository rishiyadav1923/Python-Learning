# Python File write() Method

# Example
# Open the file with "a" for appending, then add some text to the file:

f = open("demofile2.txt", "a")
f.write("See you soon!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Definition and Usage
# The write() method writes a specified text to the file.

# Where the specified text will be inserted depends on the file mode and stream position.
# "a":  The text will be inserted at the current file stream position, default at the end of the file.
# "w": The file will be emptied before the text will be inserted at the current file stream position, default 0.

# Syntax
# file.write(byte)

# Parameter Values
# Parameter	                Description
# byte	                    The text or byte object that will be inserted.

# More examples
# Example
# The same example as above, but inserting a line break before the inserted text:

f = open("demofile2.txt", "a")
f.write("\nSee you soon!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

