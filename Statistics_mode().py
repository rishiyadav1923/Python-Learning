# Python statistics.mode() Method

# Example
# Calculate the mode (central tendency) of the given data:

# Import statistics Library
import statistics

# Calculate the mode
print(statistics.mode([1, 3, 3, 3, 5, 7, 7 ,9, 11]))
print(statistics.mode([1, 1, 3, -5, 7, -9, 11]))
print(statistics.mode(['red', 'green', 'blue', 'red']))

# Definition and Usage
# The statistics.mode() method calculates the mode (central tendency) of the given numeric or nominal data set.

# Syntax
# statistics.mode(data)

# Parameter Values
# Parameter	                Description
# data	                    Required. The data values to be used (can be any sequence, list or iterator)

# *Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float or nominal value, representing the mode of the given data
# Python Version:	3.4
# Change Log:	3.8: Now handles multimodal datasets (will return the first mode encountered)

