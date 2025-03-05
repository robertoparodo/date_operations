# Advanced Date Management Library

## Overview
This library provides a set of powerful and easy-to-use methods for handling dates efficiently, using the Italian date format dd-mm-yyyy. 
It operates within the limits of the modern **Gregorian calendar** and does not support dates before year 1 AD. 
Additionally, the library enforces a strict four-digit year format, meaning that any attempt to input a year with five or more digits will result in an exception.

## Features
- Extract day, month, and year from a given date.
- Check if a year is a leap year.
- Export a date as a dictionary.
- Retrieve the current date on Windows, Linux, and iOS.
- Get the full date, including the day of the week, day, month, and year.
- Copy a date easily.
- Calculate the difference between two dates with output in:
  - Days
  - Months
  - Years
  - Weeks
  - Hours
  - Minutes
  - Seconds
- Determine the day of the week for a given date.
- Add days, months, or years to a date.
- Remove years to a date.
- Validate date existence and format.
- Compare two dates to check if one is greater than, less than, or equal to the other.
- Includes three custom error classes for better exception handling.

## Usage
Here is a basic example of how to use the library:
```python
from Date import Date

casual_date = Date("24-01-2000")
other_date = Date("10-09-1953")

print(casual_date.day)  # Output: 24
print(casual_date.is_leap)  # Output: True
print(casual_date.export_date)  # Output: {'day': 24, 'month': 01, 'year': 2000}

print(casual_date.full_date) # Output: Monday 24 January 2000

print(casual_date.days_between(other_date)) # Output: 16937
print(casual_date.months_between(other_date)) # Output: 556.44
print(other_date.years_between(casual_date)) # Output: 46.37

print(other_date.hours_between(casual_date)) # Output: 406488
print(other_date.minutes_between(casual_date)) # Output: 24389280
print(other_date.second_between(casual_date)) # Output: 1463356800

print(casual_date.get_weekday()) # Monday
```
## Author
Roberto Parodo