from date import Date


if __name__ == '__main__':

    casual_date = Date("24-01-2000")
    other_date = Date("10-09-1953")

    print(casual_date.day)  # Output: 24
    print(casual_date.is_leap)  # Output: True
    print(casual_date.export_date)  # Output: {'day': 24, 'month': 01, 'year': 2000}

    print(casual_date.full_date)  # Output: Monday 24 January 2000

    print(casual_date.days_between(other_date))  # Output: 16937
    print(casual_date.months_between(other_date))  # Output: 556.44
    print(other_date.years_between(casual_date))  # Output: 46.37

    print(other_date.hours_between(casual_date))  # Output: 406488
    print(other_date.minutes_between(casual_date))  # Output: 24389280
    print(other_date.second_between(casual_date))  # Output: 1463356800

    print(casual_date.get_weekday())  # Monday

    casual_date.add_days(100)
    print(casual_date) # Output: 03-05-2000

    casual_date.remove_days(100)
    print(casual_date) # Output: 24-01-2000