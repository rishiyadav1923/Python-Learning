# Python statistics.median_high() Method

# Example
# Calculate the high median (middle value) of the given data:

# Import statistics Library
import statistics

# Calculate the high middle values
print(statistics.median_high([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_high([1, 3, 5, 7, 9, 11]))
print(statistics.median_high([-11, 5.5, -3.4, 7.1, -9, 22]))

# Definition and Usage
# The statistics.median_high() method calculates the high median of the given data set. This method also sorts the data in ascending order before calculating the high median.

# *Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the larger of the two middle values.

# Syntax
# statistics.median_high(data)

# Parameter Values
# Parameter	                Description
# data	                    Required. The data values to be used (can be any sequence, list or iterator)

# Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the high median (middle value) of the given data
# Python Version:	3.4

