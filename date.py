"""
Advanced Date Management Library

This library provides a set of useful methods for working with dates in a simple and efficient way, using the Italian format dd-mm-yyyy.

Features:
- Retrieve the day, month, and year from a given date
- Check if a year is a leap year
- Export a date as a dictionary
- Get the current date across Windows, Linux, and iOS systems
- Return the full date, including the day of the week, day, month, and year
- Copy a date easily
- Calculate the difference between two dates with output in days, months, years, weeks, hours, minutes, and seconds
- Given a date, determine the corresponding day of the week
- Add days, months, or years to a date
- Remove days, months, or years to a date
- Validate date existence and format
- Includes three custom error classes for exception handling
- Compare two dates to determine whether one is greater than, less than, or equal to the other

This library is ideal for anyone needing flexible date operations in their Python projects.
It offers greater simplicity compared to the standard datetime module.

Author: Roberto Parodo
"""
from custom_exceptions import InvalidDateError, InvalidDateFormatError, InvalidDateRemove, InvalidDateAdd
import re, os

CALENDAR = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
MONTH_DAYS = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
WEEKDAYS = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

def from_month_to_days(year, month) -> int:
    return MONTH_DAYS[CALENDAR[month]] if month != 2 else 29 if year % 4 == 0 and (
                year % 100 != 0 or year % 400 == 0) else 28

class Date:
    def __init__(self, date: str):
        """
           Initializes the Date instance.
           Args:
               date (str): The date string in dd-mm-yyyy format.
           Raises:
               ValueError: If the date format is invalid.
        """
        self.__date = date
        self.__validate_date()

    @property
    def day(self) -> int:
        """
        Given a date
        :return: day in number format
        """
        return int(self.__date[:2])

    @property
    def month(self) -> int:
        """
        Given a date
        :return: month in number format
        """
        return int(self.__date[3:5])

    @property
    def year(self) -> int:
        """
        Given a date
        :return: year in number format
        """
        return int(self.__date[6::])

    @property
    def export_date(self) -> dict:
        """
        Given a date
        :return: a dictionary of the date
        """
        return {"day":self.day, "month": self.month, "year": self.year}

    @property
    def is_leap(self) -> bool:
        """
        Checks if the stored year is a leap year.
        :return:
            bool: True if the year is a leap year, False otherwise.
        """
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    @property
    def today(self) -> str:
        """
        Calls method to today's date
        :return: in string format
        """
        if os.name == "nt":
            return os.popen("date /T").read().strip().replace("/","-")
        return os.popen("date '+%d-%m-%Y'").read().strip()

    @property
    def full_date(self) -> str:
        """
        Get the full date, including the day of the week, day, month, and year.
        :return: full date in string format
        """
        return self.get_weekday()+" "+str(self.day)+" "+CALENDAR[self.month]+" "+str(self.year)

    @property
    def century(self) -> int:
        """
        Returns the century in which the year is located
        :return: the century
        """
        return ((self.year-1)//100) + 1

    def copy(self):
        """
        Create a copy of the date
        :return: a new Date object
        """
        return Date(self.__date)

    def __validate_date(self) -> None:
        """
        Private method to check that a new possible date is correct or exist
        :return: None
        """
        pattern = r"^\d{2}-\d{2}-\d{4}$"
        if not re.match(pattern, self.__date):
            raise InvalidDateFormatError(self.__date)
        if self.month < 1 or self.month > 12:
            raise InvalidDateError(self.__date)
        if self.day < 1 or self.day > MONTH_DAYS[CALENDAR[self.month]]:
            if self.month == 2:
                if self.day > (29 if self.is_leap else 28):
                    raise InvalidDateError(self.__date)
            else:
                raise InvalidDateError(self.__date)

    def second_between(self, other) -> int:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in seconds
        """
        return self.days_between(other) * 24 * 60 * 60

    def minutes_between(self, other) -> int:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in minutes
        """
        return self.days_between(other) * 24 * 60

    def hours_between(self, other) -> int:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in hours
        """
        return self.days_between(other) * 24

    def days_between(self, other) -> int:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in days
        """
        if type(other) == str: other = Date(other)
        if self.__eq__(other): return 0
        if self.year == other.year and self.month == other.month: return abs(self.day - other.day)
        if self.__gt__(other):
            bigger, smaller = self.copy(), other.copy()
        else:
            bigger, smaller = other.copy(), self.copy()
        year_difference = (bigger.year - smaller.year)*12
        if bigger.month < smaller.month:
            month_difference = smaller.month - bigger.month
            year_difference = year_difference - month_difference
        elif bigger.month > smaller.month:
            month_difference = bigger.month - smaller.month
            year_difference = year_difference + month_difference
        counter = 0
        timeline = [{"month": smaller.month, "year": smaller.year}]
        while counter < year_difference:
            last_month = timeline[-1]["month"]
            last_year = timeline[-1]["year"]
            if last_month == 12:
                timeline.append({"month": 1, "year": last_year+1})
            else:
                timeline.append({"month": last_month+1, "year": last_year})
            counter += 1
        days = from_month_to_days(timeline[0]["year"], timeline[0]["month"])-smaller.day
        timeline.pop(0)
        days += bigger.day
        timeline.pop(-1)
        for date in timeline:
            days += from_month_to_days(date["year"], date["month"])
        return days

    def week_between(self, other)-> float:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in weeks
        """
        return round(self.days_between(other)/7, 2)

    def months_between(self, other) -> float:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in months
        """
        if type(other) == str: other = Date(other)
        if self.year == other.year and self.month == other.month: return 0
        if self.year==other.year and self.day == other.day: return abs(self.month-other.month)
        if self.__gt__(other):
            bigger, smaller = self.copy(), other.copy()
        else:
            bigger, smaller = other.copy(), self.copy()
        months = (bigger.year - smaller.year)*12
        days_month_smaller = smaller.day / from_month_to_days(smaller.year, smaller.month)
        days_month_bigger = bigger.day/from_month_to_days(bigger.year, bigger.month)
        if bigger.month >= smaller.month:
            months += bigger.month - smaller.month - days_month_smaller + days_month_bigger
        else:
            months -= smaller.month - bigger.month + days_month_smaller - days_month_bigger
        return round(months, 2)

    def years_between(self, other) -> float:
        """
        Method to calculate the difference between two dates
        :param other: is a different date to compare
        :return: difference in years
        """
        if type(other) == str: other = Date(other)
        if self.__eq__(other): return 0
        if self.month==other.month and self.day == other.day: return abs(self.year-other.year)
        if self.__gt__(other):
            bigger, smaller = self.copy(), other.copy()
        else:
            bigger, smaller = other.copy(), self.copy()
        smaller_day_to_year = (smaller.day/from_month_to_days(smaller.year, smaller.month))/12
        bigger_day_to_year = (bigger.day/from_month_to_days(bigger.year, bigger.month))/12
        year_difference = bigger.year - smaller.year
        if bigger.month >= smaller.month:
            month_difference = (bigger.month-smaller.month)/12
            year_difference += month_difference-smaller_day_to_year+bigger_day_to_year
        else:
            month_difference = (smaller.month-bigger.month)/12
            year_difference -= month_difference+smaller_day_to_year-bigger_day_to_year
        return round(year_difference, 2)

    def add_years(self, years: int) -> None:
        """
        Adds the specified number of years to the current date.
        :param years: The number of years to add to the date.
        :return: None. The original date is modified in place.
        """
        if type(years) == str or years < 0 or len(str(self.year+years))>=5: raise InvalidDateAdd(years)
        new_year = str(self.year+years)
        self.__set_date(self.__date[:6]+new_year)

    def remove_years(self, years: int) -> None:
        """
        Removes the specified number of years to the current date.
        :param years: The number of years to remove to the date.
        :return: None. The original date is modified in place.
        """
        if type(years) == str or years < 0 or self.year < years: raise InvalidDateRemove(years)
        new_year = str(self.year-years)
        if len(new_year) < 4: new_year = "0"*(4-len(new_year))+new_year
        self.__set_date(self.__date[:6]+new_year)

    def add_months(self, months: int) -> None:
        """
        Adds the specified number of months to the current date.
        :param months: The number of months to add to the date.
        :return: None. The original date is modified in place.
        """
        if type(months) == str or months < 0: raise InvalidDateAdd(months)
        month = 1
        while month <= months:
            if self.month == 12:
                self.add_years(1)
                new_day= "0"+str(self.day) if len(str(self.day)) == 1 else str(self.day)
                self.__set_date(new_day+"-"+"01"+"-"+str(self.year))
            else:
                new_month = str(self.month+1)
                new_day = "0" + str(self.day) if len(str(self.day)) == 1 else str(self.day)
                if len(new_month) == 1: new_month = "0"+new_month
                self.__set_date(new_day+"-"+new_month+"-"+str(self.year))
            month += 1

    def remove_months(self, months: int) -> None:
        """
        Removes the specified number of months to the current date.
        :param months: The number of months to remove to the date.
        :return: None. The original date is modified in place.
        """
        if type(months) == str or months < 0: raise InvalidDateRemove(months)
        month = 1
        while month <= months:
            if self.month == 1:
                self.remove_years(1)
                new_day= "0"+str(self.day) if len(str(self.day)) == 1 else str(self.day)
                self.__set_date(new_day+"-"+"12"+"-"+str(self.year))
            else:
                new_month = str(self.month-1)
                new_day = "0" + str(self.day) if len(str(self.day)) == 1 else str(self.day)
                if len(new_month) == 1: new_month = "0"+new_month
                self.__set_date(new_day+"-"+new_month+"-"+str(self.year))
            month += 1

    def add_days(self, days: int) -> None:
        """
        Adds the specified number of days to the current date.
        :param days: The number of days to add to the date.
        :return: None. The original date is modified in place.
        """
        if type(days) == str or days < 0: raise InvalidDateAdd(days)
        day = 1
        while day <= days:
            if self.day == from_month_to_days(self.year, self.month):
                self.add_months(1)
                self.__set_date("01"+"-"+self.__date[3:5]+"-"+str(self.year))
            else:
                new_day = str(self.day+1)
                if len(new_day) == 1: new_day = "0"+new_day
                self.__set_date(new_day+"-"+self.__date[3:5]+"-"+str(self.year))
            day += 1

    def remove_days(self, days: int) -> None:
        """
        Removes the specified number of days to the current date.
        :param days: The number of days to remove to the date.
        :return: None. The original date is modified in place.
        """
        if type(days) == str or days < 0: raise InvalidDateRemove(days)
        day = 1
        while day <= days:
            if self.day == 1:
                self.remove_months(1)
                self.__set_date(str(from_month_to_days(self.year, self.month))+"-"+self.__date[3:5]+"-"+str(self.year))
            else:
                new_day = str(self.day-1)
                if len(new_day) == 1: new_day = "0"+new_day
                self.__set_date(new_day+"-"+self.__date[3:5]+"-"+str(self.year))
            day += 1

    def get_weekday(self) -> str:
        """
        Returns the name of the weekday for the current date.
        :return: A string representing the day of the week (e.g., 'Monday', 'Tuesday').
        """
        reference_date = Date("24-01-2000")
        return self.__calculate_week(reference_date, True) if self.__gt__(reference_date) \
            else self.__calculate_week(reference_date, False)

    def __calculate_week(self, other, flag: bool) -> str:
        """
        Private method that returns the weekday relative to a reference date.
        :param other: The reference date used to calculate the weekday. This parameter is invisible to the user (e.g., 24-01-2000 is Monday).
        :param flag: If True, the counting moves forward (from the reference day). If False, the counting moves backward.
        :return: The weekday as a string (e.g., 'Monday', 'Tuesday', etc.).
        """
        day_difference = self.days_between(other)
        week, index = 0, 1
        if flag:
            while week < day_difference:
                index += 1
                if index > 7:
                    index = 1
                week += 1
        else:
            while week < day_difference:
                index -= 1
                if index == 0:
                    index = 7
                week += 1
        return WEEKDAYS[index]

    def __set_date(self, date) -> None:
        """
        Private method that modify the date.
        :param date: update the old date
        :return: None
        """
        self.__date = date

    def __eq__(self, other) -> bool:
        """
        Compares the current object with another object to determine if they are equal.
        :param other: The object to compare with the current object.
        :return: True if the objects are equal, False otherwise.
        """
        return self.__date == other.__date

    def __gt__(self, other) -> bool:
        """
        Compares the current object with another object to determine if it is greater.
        :param other: The object to compare with the current object.
        :return: True if the current object is greater than the other object, False otherwise.
        """
        if self.__eq__(other): return False
        if self.year > other.year: return True
        if self.year == other.year:
            if self.month > other.month: return True
            if self.month == other.month:
                if self.day > other.day: return True
        return False

    def __lt__(self, other) -> bool:
        """
        Compares the current object with another object to determine if it is lesser.
        :param other: The object to compare with the current object.
        :return: True if the current object is lesser than the other object, False otherwise.
        """
        if self.__eq__(other): return False
        if self.year < other.year: return True
        if self.year == other.year:
            if self.month < other.month: return True
            if self.month == other.month:
                if self.day < other.day: return True
        return False

    def __ge__(self, other) -> bool:
        """
        Compares the current object with another object to determine if it is greater than or equal.
        :param other: The object to compare with the current object.
        :return: True if the current object is greater than or equal to the other object, False otherwise.
        """
        if self.__eq__(other): return True
        if self.year > other.year: return True
        if self.year == other.year:
            if self.month > other.month: return True
            if self.month == other.month:
                if self.day > other.day: return True
        return False

    def __le__(self, other)-> bool:
        """
        Compares the current object with another object to determine if it is lesser than or equal.
        :param other: The object to compare with the current object.
        :return: True if the current object is lesser than or equal to the other object, False otherwise.
        """
        if self.__eq__(other): return True
        if self.year < other.year: return True
        if self.year == other.year:
            if self.month < other.month: return True
            if self.month == other.month:
                if self.day < other.day: return True
        return False

    def __str__(self) -> str:
        """
        Returns a string representation of the current object.
        :return: A string that describes the current object in string format.
        """
        return self.__date