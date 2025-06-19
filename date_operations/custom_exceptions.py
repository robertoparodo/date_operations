class InvalidDateFormatError(Exception):
    def __init__(self, date):
        super().__init__(f"Invalid date format: '{date}'. Use the format: 'dd-mm-yyyy'.")

class InvalidDateError(Exception):
    def __init__(self, date):
        super().__init__(f"Invalid date: '{date}'. Doesn't exist.")

class InvalidDateAdd(Exception):
    def __init__(self, date):
        super().__init__(f"Invalid date: '{date}'. Cannot add negative numbers, strings or an excessively large number of years.")

class InvalidDateRemove(Exception):
    def __init__(self, date):
        super().__init__(f"Invalid date: '{date}'. Cannot add negative numbers, strings or years larger than the date.")
