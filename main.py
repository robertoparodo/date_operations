from Date import Date

if __name__ == '__main__':
    casual_date = Date("28-10-1942")
    other_date = Date("04-03-2025")

    #print(casual_date.today)

    #print(other_date.get_weekday())
    casual_date.add_months(96057)
    print(casual_date)