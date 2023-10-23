def other_method(val):
    print(f"other_method: {val}")

class Date(object):
    def __init__(self, Year, Month, Day):
        self.year  = Year
        self.month = Month
        self.day   = Day

    def __str__(self):
        return f'Date({self.year}, {self.month}, {self.day})'

    @classmethod
    def from_str(cls, date_str):
        '''Call as
           d = Date.from_str('2013-12-30')
        '''
        print(f"from_str: {cls}")
        year, month, day = map(int, date_str.split('-'))

        other_method(43)

        if cls.is_valid_date(year, month, day):
            return cls(year, month, day)
        else:
            raise Exception("Invalid date")

    @staticmethod
    def is_valid_date(year, month, day):
        return 0 <= year <= 3000 and 1 <= month <= 12 and 1 <= day <= 31

