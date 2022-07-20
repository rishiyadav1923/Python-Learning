# Python statistics.variance() Method

# Example
# Calculate the variance from a sample of data:

# Import statistics Library
import statistics

# Calculate the variance from a sample of data
print(statistics.variance([1, 3, 5, 7, 9, 11]))
print(statistics.variance([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.variance([-11, 5.5, -3.4, 7.1]))
print(statistics.variance([1, 30, 50, 100]))

# Definition and Usage
# The statistics.variance() method calculates the variance from a sample of data (from a population).
# A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean.

# *Tip: To calculate the variance of an entire population, look at the statistics.pvariance() method.

# Syntax
# statistics.variance(data, xbar)

# Parameter Values
# Parameter	                Description
# data	                    Required. The data values to be used (can be any sequence, list or iterator)
# xbar	                    Optional. The mean of the given data. If omitted (or set to None), the mean is automatically calculated

# *Note: If data has less than two values, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the sample variance of the given data
# Python Version:	3.4

