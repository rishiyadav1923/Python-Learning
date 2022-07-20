# Python statistics.median_low() Method

# Example
# Calculate the low median (middle value) of the given data:

# Import statistics Library
import statistics

# Calculate the low middle values
print(statistics.median_low([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median_low([1, 3, 5, 7, 9, 11]))
print(statistics.median_low([-11, 5.5, -3.4, 7.1, -9, 22]))

# Definition and Usage
# The statistics.median_low() method calculates the low median of the given data set. This method also sorts the data in ascending order before calculating the low median.

# *Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the smaller of the two middle values.

# Syntax
# statistics.median_low(data)

# Parameter Values
# Parameter	            Description
# data	                Required. The data values to be used (can be any sequence, list or iterator)

# *Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the low median (middle value) of the given data
# Python Version:	3.4

