# Python statistics.mean() Method

# Example
# Calculate the average of the given data:

# Import statistics Library
import statistics

# Calculate average values
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print(statistics.mean([1, 3, 5, 7, 9, 11]))
print(statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22]))

# Definition and Usage
# The statistics.mean() method calculates the mean (average) of the given data set.

# *Tip: Mean = add up all the given values, then divide by how many values there are.

# Syntax
# statistics.mean(data)

# Parameter Values
# Parameter	                Description
# data	                    Required. The data values to be used (can be any sequence, list or iterator)

# *Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the average of the given data
# Python Version:	3.4

