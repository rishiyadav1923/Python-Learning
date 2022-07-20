# Python statistics.stdev() Method

# Example
# Calculate the standard deviation of the given data:

# Import statistics Library
import statistics

# Calculate the standard deviation from a sample of data
print(statistics.stdev([1, 3, 5, 7, 9, 11]))
print(statistics.stdev([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.stdev([-11, 5.5, -3.4, 7.1]))
print(statistics.stdev([1, 30, 50, 100]))

# Definition and Usage
# The statistics.stdev() method calculates the standard deviation from a sample of data.
# Standard deviation is a measure of how spread out the numbers are.
# A large standard deviation indicates that the data is spread out, - a small standard deviation indicates that the data is clustered closely around the mean.

# *Tip: Standard deviation is (unlike the Variance) expressed in the same units as the data.

# *Tip: Standard deviation is the square root of sample variance.

# *Tip: To calculate the standard deviation of an entire population, look at the statistics.pstdev() method. 

# Syntax
# statistics.stdev(data, xbar)

# Parameter Values
# Parameter	            Description
# data	                Required. The data values to be used (can be any sequence, list or iterator)
# xbar	                Optional. The mean of the given data. If omitted (or set to None), the mean is automatically calculated

# *Note: If data has less than two values, it returns a StatisticsError. 

# Technical Details
# Return Value:	A float value, representing the standard deviation of the given data
# Python Version:	3.4

