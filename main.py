from Date import Date

if __name__ == '__main__':
    casual_date = Date("28-10-1942")
    other_date = Date("05-03-2025")

    #print(casual_date.today)

    #print(other_date.get_weekday())
    other_date.remove_days(3612)
    print(other_date.full_date)
