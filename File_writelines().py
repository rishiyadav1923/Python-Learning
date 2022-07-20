# Python File writelines() Method

# Example
# Open the file with "a" for appending, then add a list of texts to append to the file:

f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

# Definition and Usage
# The writelines() method writes the items of a list to the file.

# Where the texts will be inserted depends on the file mode and stream position.
# "a":  The texts will be inserted at the current file stream position, default at the end of the file.
# "w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.

# Syntax
# file.writelines(list)

# Parameter Values
# Parameter	            Description
# list	                The list of texts or byte objects that will be inserted.

# More examples
# Example
# The same example as above, but inserting line breaks for each list item:

f = open("demofile3.txt", "a")
f.writelines(["\nSee you soon!", "\nOver and out."])
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

