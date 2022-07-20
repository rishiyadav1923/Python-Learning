# Python Datetime

# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# Example
# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

# Date Output
# When we execute the code from the example above the result will be:

# 2022-07-10 23:14:49.281849

# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.
# Here are a few examples, you will learn more about them later in this chapter:

# Example
# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

# Example
# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).


# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# Example
# Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# A reference of all the legal format codes:

import datetime

# Directive	            Description	                                                    Example

# %a	                Weekday, short version	                                          Wed
x = datetime.datetime.now()
print(x.strftime("%a"))

# %A	                Weekday, full version	                                       Wednesday
x = datetime.datetime.now()
print(x.strftime("%A"))

# %w	                Weekday as a number 0-6, 0 is Sunday	                           3
x = datetime.datetime.now()
print(x.strftime("%w"))

# %d	                Day of month 01-31	                                               31
x = datetime.datetime.now()
print(x.strftime("%d"))

# %b	                Month name, short version	                                      Dec
x = datetime.datetime.now()
print(x.strftime("%b"))

# %B	                Month name, full version	                                   December
x = datetime.datetime.now()
print(x.strftime("%B"))

# %m	                Month as a number 01-12	                                           12
x = datetime.datetime.now()
print(x.strftime("%m"))

# %y	                Year, short version, without century	                           18
x = datetime.datetime.now()
print(x.strftime("%y"))

# %Y	                Year, full version	                                              2018
x = datetime.datetime.now()
print(x.strftime("%Y"))

# %H	                Hour 00-23	                                                       17
x = datetime.datetime.now()
print(x.strftime("%H"))

# %I	                Hour 00-12	                                                       05
x = datetime.datetime.now()
print(x.strftime("%I"))

# %p	                AM/PM	                                                           PM
x = datetime.datetime.now()
print(x.strftime("%p"))

# %M	                Minute 00-59	                                                   41
x = datetime.datetime.now()
print(x.strftime("%M"))

# %S	                Second 00-59	                                                   08
x = datetime.datetime.now()
print(x.strftime("%S"))

# %f	                Microsecond 000000-999999	                                     548513
x = datetime.datetime.now()
print(x.strftime("%f"))

# %z	                UTC offset	                                                     +0100
x = datetime.datetime.now()
print(x.strftime("%z"))

# %Z	                Timezone	                                                      CST
x = datetime.datetime.now()
print(x.strftime("%Z"))

# %j	                Day number of year 001-366	                                      365
x = datetime.datetime.now()
print(x.strftime("%j"))

# %U	                Week number of year, Sunday as the first day of week, 00-53	       52
x = datetime.datetime.now()
print(x.strftime("%U"))

# %W	                Week number of year, Monday as the first day of week, 00-53	       52
x = datetime.datetime.now()
print(x.strftime("%W"))

# %c	                Local version of date and time	                        Mon Dec 31 17:41:00 2018
x = datetime.datetime.now()
print(x.strftime("%c"))

# %C	                Century	                                                           20
x = datetime.datetime.now()
print(x.strftime("%C"))

# %x	                Local version of date	                                        12/31/18
x = datetime.datetime.now()
print(x.strftime("%x"))

# %X	                Local version of time	                                        17:41:00
x = datetime.datetime.now()
print(x.strftime("%X"))

# *%%	                A % character	                                                    %
x = datetime.datetime.now()
print(x.strftime("%%"))

# %G	                ISO 8601 year	                                                   2018
x = datetime.datetime.now()
print(x.strftime("%G"))

# %u	                ISO 8601 weekday (1-7)	                                            1
x = datetime.datetime.now()
print(x.strftime("%u"))

# %V	                ISO 8601 week-number (01-53)	                                        01
x = datetime.datetime.now()
print(x.strftime("%V"))
