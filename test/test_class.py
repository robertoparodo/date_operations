from date_operations.custom_exceptions import InvalidDateError, InvalidDateFormatError, InvalidDateRemove, InvalidDateAdd

from date_operations import Date
import pytest

def test_data_day():
    date = Date("24-01-2000")
    assert date.day == 24

def test_data_month():
    date = Date("24-01-2000")
    assert date.month == 1

def test_data_year():
    date = Date("24-01-2000")
    assert date.year == 2000

def test_data_is_leap():
    date = Date("24-01-2000")
    assert date.is_leap == True

def test_export_date():
    date = Date("24-01-2000")
    assert date.export_date == {'day': 24, 'month': 1, 'year': 2000}

def test_full_date():
    date = Date("24-01-2000")
    assert type(date.full_date) == str
    assert date.full_date == "Monday 24 January 2000"

def test_data_days_between():
    date = Date("24-01-2000")
    other_date = Date("10-09-1953")
    assert date.days_between(other_date) == 16937
    assert type(date.days_between(other_date)) == int

def test_data_months_between():
    date = Date("24-01-2000")
    other_date = Date("10-09-1953")
    assert date.months_between(other_date) == 556.44
    assert type(date.days_between(other_date)) == int

def test_data_years_between():
    date = Date("24-01-2000")
    other_date = Date("10-09-1953")
    assert date.years_between(other_date) == 46.37
    assert type(date.days_between(other_date)) == int

def test_data_hours_between():
    date = Date("24-01-2000")
    other_date = Date("10-09-1953")
    assert date.hours_between(other_date) == 406488
    assert type(date.days_between(other_date)) == int

def test_data_minutes_between():
    date = Date("24-01-2000")
    other_date = Date("10-09-1953")
    assert date.minutes_between(other_date) == 24389280
    assert type(date.days_between(other_date)) == int

def test_data_second_between():
    date = Date("24-01-2000")
    other_date = Date("10-09-1953")
    assert date.second_between(other_date) == 1463356800
    assert type(date.days_between(other_date)) == int

def test_get_weekday():
    date = Date("24-01-2000")
    assert date.get_weekday() == "Monday"

def test_century():
    date = Date("24-01-2000")
    assert date.century == 20

def test_error_format():
    with pytest.raises(InvalidDateFormatError):
        date = Date("24/01/2000")

def test_error_format():
    with pytest.raises(InvalidDateFormatError):
        date = Date("2000-12-24")

def test_date_error():
    with pytest.raises(InvalidDateError):
        date = Date("01-31-2000")