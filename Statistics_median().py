# Python statistics.median() Method

# Example
# Calculate the median (middle value) of the given data:

# Import statistics Library
import statistics

# Calculate middle values
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([1, 3, 5, 7, 9, 11]))
print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))

# Definition and Usage
# The statistics.median() method calculates the median (middle value) of the given data set. This method also sorts the data in ascending order before calculating the median.

# *Tip: The mathematical formula for Median is: Median = {(n + 1) / 2}th value, where n is the number of values in a set of data. In order to calculate the median, the data must first be sorted in ascending order. The median is the number in the middle.

# *Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the average of the two middle values.

# Syntax
# statistics.median(data)

# Parameter Values
# Parameter	                Description
# data	                    Required. The data values to be used (can be any sequence, list or iterator)

# Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the median (middle value) of the given data
# Python Version:	3.4

