# Python statistics.harmonic_mean() Method

# Example
# Calculate the harmonic mean of the given data:

# Import statistics Library
import statistics

# Calculate harmonic mean
print(statistics.harmonic_mean([40, 60, 80]))
print(statistics.harmonic_mean([10, 30, 50, 70, 90]))

# Definition and Usage
# The statistics.harmonic_mean() method calculates the harmonic mean (central location) of the given data set.
# Harmonic mean = The reciprocal of the arithmetic mean() of the reciprocals of the data.
# The harmonic mean is calculated as follows:
# If you have four values (a, b, c and d) - it will be equivalent to 4 / (1/a + 1/b + 1/c + 1/d).

# Syntax
# statistics.harmonic_mean(data)

# Parameter Values
# Parameter	            Description
# data	                Required. The data values to be used 
#                       (can be any sequence, list or iterator). Note: Cannot contain negative values!

# *Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the harmonic mean of the given data
# Python Version:	3.6
