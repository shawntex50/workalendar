from ..core import ChineseNewYearCalendar
from ..registry_tools import iso_register


@iso_register('KR')
class SouthKorea(ChineseNewYearCalendar):
    "South Korea"
    FIXED_HOLIDAYS = ChineseNewYearCalendar.FIXED_HOLIDAYS + (
        (3, 1, "Independence Day"),
        (5, 5, "Children's Day"),
        (6, 6, "Memorial Day"),
        (8, 15, "Liberation Day"),
        (10, 3, "National Foundation Day"),
        (10, 9, "Hangul Day"),
        (12, 25, "Christmas Day"),
    )
    chinese_new_year_label = "Korean New Year's Day"
    include_chinese_new_year_eve = True
    chinese_new_year_eve_label = "Korean New Year's Day"
    include_chinese_second_day = True
    chinese_second_day_label = "Korean New Year's Day"

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        days.extend([
            (ChineseNewYearCalendar.lunar(year, 4, 8), "Buddha's Birthday"),
            # Midautumn Festival (3 days)
            (ChineseNewYearCalendar.lunar(year, 8, 14), "Midautumn Festival"),
            (ChineseNewYearCalendar.lunar(year, 8, 15), "Midautumn Festival"),
            (ChineseNewYearCalendar.lunar(year, 8, 16), "Midautumn Festival"),
        ])

        #if year == 2023:
        days.append((ChineseNewYearCalendar.lunar(year, 1, 1), "Seollal (Korean New Year)"))
        return days
