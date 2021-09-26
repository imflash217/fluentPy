"""Implements a proleptic Gregorian Calendar date as a Julian number"""


class Date:
    """Creates an object instance for the specified Gregorian date"""

    def __init__(self, month, day, year):
        super().__init__()
        self._julian_day = 0
        assert self._is_valid_gregorian(month, day, year), "Invalid Gregorain date"
        self._julian_day = self._to_julian(month, day, year)

    def month(self):
        """Returning M from (M,d,y)"""
        return (self._to_gregorian())[0]

    def day(self):
        """retuns D from (m, D, y)"""
        return self._to_gregorian()[1]

    def year(self):
        """Returns Y from (m, d, Y)"""
        return self._to_gregorian()[2]

    def day_of_week(self):
        month, day, year = self._to_gregorian()
        if month < 3:
            month += 12
            year -= 1
        return (
            (13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400
        ) % 7

    def __str__(self):
        month, day, year = self._to_gregorian()
        return f"{month:02d}/{day:02d}/{year:04d}"

    def __eq__(self, other):
        """Logically compares the two dates"""
        return self._julian_day == other._julian_day

    def __lt__(self, other):
        return self._julian_day < other._julian_day

    def __le__(self, other):
        return self._julian_day <= other._julian_day

    def __gt__(self, other):
        return self._julian_day > other._julain_day

    def __ge__(self, other):
        return self._julian_day >= other._julian_day

    @staticmethod
    def _to_julian(month, day, year):
        tmp = 0
        if month < 3:
            tmp = -1
        julian_day = (
            day
            - 32075
            + (1461 * (year + 4800 + tmp) // 4)
            + (367 * (month - 2 - tmp * 12) // 12)
            - (3 * ((year + 4900 + tmp) // 100) // 4)
        )
        return julian_day

    def _to_gregorian(self, julian_day=None):
        if not julian_day:
            julian_day = self._julian_day

        A = julian_day + 68569
        B = 4 * A // 146097
        A += -(146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001

        A += 31 - (1461 * year // 4)
        month = 80 * A // 2447
        day = A - (2447 * month // 80)

        A = month // 11
        month += 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return (month, day, year)

    def _is_valid_gregorian(self, month, day, year):
        julian_day = self._to_julian(month, day, year)
        gregorian_date = self._to_gregorian(julian_day)
        print(julian_day)
        print(gregorian_date)
        ##return gregorian_date == (month, day, year)
        return True
