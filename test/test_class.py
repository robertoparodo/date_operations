from date_operations import Date

def test_data_day():
    date = Date("24-01-2000")
    assert date.day == 24

def test_data_month():
    date = Date("24-01-2000")
    assert date.month == 1

def test_data_year():
    date = Date("24-01-2000")
    assert date.year == 2000
