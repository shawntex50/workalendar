from datetime import date

from . import GenericCalendarTest
from ..europe import Ireland


class IrelandTest(GenericCalendarTest):
    cal_class = Ireland

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)    # New Year
        self.assertIn(date(2020, 3, 17), holidays)   # Saint Patrick's Day
        self.assertIn(date(2020, 4, 13), holidays)   # Easter Monday
        self.assertIn(date(2020, 5, 4), holidays)    # May Day
        self.assertIn(date(2020, 6, 1), holidays)    # June Holiday
        self.assertIn(date(2020, 8, 3), holidays)    # August Holiday
        self.assertIn(date(2020, 10, 26), holidays)  # October Holiday
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas
        self.assertIn(date(2020, 12, 26), holidays)  # St. Stephen's Day
        self.assertIn(date(2020, 12, 28), holidays)  # St. Stephen's Day Shift

    def test_year_2024(self):
        holidays = self.cal.holidays_set(2024)
        self.assertIn(date(2024, 1, 1), holidays)    # New Year
        self.assertIn(date(2024, 2, 5), holidays)    # St. Brigid's Day
        self.assertIn(date(2024, 3, 17), holidays)   # Saint Patrick's Day
        self.assertIn(date(2024, 3, 17), holidays)   # Saint Patrick's Day substitute
        self.assertIn(date(2024, 4, 1), holidays)    # Easter Monday
        self.assertIn(date(2024, 5, 6), holidays)    # May Day
        self.assertIn(date(2024, 6, 3), holidays)    # June Holiday
        self.assertIn(date(2024, 8, 5), holidays)    # August Holiday
        self.assertIn(date(2024, 10, 28), holidays)  # October Holiday
        self.assertIn(date(2024, 12, 25), holidays)  # Christmas
        self.assertIn(date(2024, 12, 26), holidays)  # St. Stephen's Day
