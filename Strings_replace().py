# Python String replace() Method

# Example
# Replace the word "bananas":

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

# Definition and Usage
# The replace() method replaces a specified phrase with another specified phrase.

# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

# Syntax
# string.replace(oldvalue, newvalue, count)

# Parameter Values
# Parameter	                    Description
# oldvalue	                    Required. The string to search for
# newvalue	                    Required. The string to replace the old value with
# count	                        Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# More Examples
# Example
# Replace all occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

# Example
# Replace the two first occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

