# Python statistics.pstdev() Method

# Example
# Calculate the standard deviation from an entire population:

# Import statistics Library
import statistics

# Calculate the standard deviation from an entire population
print(statistics.pstdev([1, 3, 5, 7, 9, 11]))
print(statistics.pstdev([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.pstdev([-11, 5.5, -3.4, 7.1]))
print(statistics.pstdev([1, 30, 50, 100]))

# Definition and Usage
# The statistics.pstdev() method calculates the standard deviation from an entire population.
# Standard deviation is a measure of how spread out the numbers are.
# A large standard deviation indicates that the data is spread out, - a small standard deviation indicates that the data is clustered closely around the mean.

# *Tip: Standard deviation is (unlike the Variance) expressed in the same units as the data.

# *Tip: Standard deviation is the square root of sample variance.

# *Tip: To calculate the standard deviation from a sample of data, look at the statistics.stdev() method. 

# Syntax
# statistics.pstdev(data, xbar)

# Parameter Values
# Parameter	            Description
# data	                Required. The data values to be used (can be any sequence, list or iterator)
# xbar	                Optional. The mean of the given data (can also be a second moment around a point that is not the mean). If omitted (or set to None), the mean is automatically calculated

# *Note: If data is empty, it returns a StatisticsError.

# Technical Details
# Return Value:	A float value, representing the population standard deviation of the given data
# Python Version:	3.4

