# Python Random setstate() Method

# Example
# Capture and restore the state of the random number generator:

import random

#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())

# Definition and Usage
# The setstate() method is used to restore the state of the random number generator back to the specified state
# Use the getstate() method to capture the state

# Syntax
# random.setstate(state)

# Parameter Values
# Parameter	            Description
# state	                Required. A state object. the setstate() method will restore the state of 
#                       the random number generator back to this sate.

