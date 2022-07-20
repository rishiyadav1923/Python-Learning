# Python statistics.pvariance() Method

# Example
# Calculate the variance of an entire population:

# Import statistics Library
import statistics

# Calculate the variance of an entire population
print(statistics.pvariance([1, 3, 5, 7, 9, 11]))
print(statistics.pvariance([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.pvariance([-11, 5.5, -3.4, 7.1]))
print(statistics.pvariance([1, 30, 50, 100]))

# Definition and Usage
# The statistics.pvariance() method calculates the variance of an entire population.
# A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean.

# *Tip: To calculate the variance from a sample of data, look at the statistics.variance() method.

# Syntax
# statistics.pvariance(data, xbar)

# Parameter Values
# Parameter	            Description
# data	                Required. The data values to be used (can be any sequence, list or iterator)
# xbar	                Optional. The mean of the given data (can also be a second moment around a point that is not the mean). If omitted (or set to None), the mean is automatically calculated

# *Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the population variance of the given data
# Python Version:	3.4

