# Python open() Function

# Example
# Open a file and print the content:

f = open("demofile.txt", "r")
print(f.read())

# Definition and Usage
# The open() function opens a file, and returns it as a file object.

# Read more about file handling in our chapters about File Handling.

# Syntax
# open(file, mode)

# Parameter Values
# Parameter	                Description

# file	                    The path and name of the file

# mode	                    A string, define which mode you want to open the file in:
#                           "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#                           "a" - Append - Opens a file for appending, creates the file if it does not exist
#                           "w" - Write - Opens a file for writing, creates the file if it does not exist
#                           "x" - Create - Creates the specified file, returns an error if the file exist

#                           In addition you can specify if the file should be handled as binary or text mode

#                           "t" - Text - Default value. Text mode
#                           "b" - Binary - Binary mode (e.g. images)

# Related Pages
# Learn how to open files in our Read Files Tutorial

# Learn how to write/create files in our Write/Create Files Tutorial

# Learn how to delete files in our Delete Files Tutorial


