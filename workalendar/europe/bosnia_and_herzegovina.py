from ..core import WesternCalendar, MON, SAT, SUN
from ..registry_tools import iso_register
from datetime import date


@iso_register('BA')
class BosniaAndHerzegovina(WesternCalendar):
    'Bosnia and Herzegovina'

    include_easter_monday = False
    include_boxing_day = True
    shift_new_years_day = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "New Years Day (Day 2)"),
        (3, 1, "Independence Day"),
        (11, 25, "Statehood Day"),
    )

    def get_fixed_holidays(self, year):
        days = super().get_fixed_holidays(year)

        labor_day = date(year, 5, 1)
        if labor_day.weekday() == SAT:
            days.append((labor_day, "Labor Day"))
            days.append((date(year, 5, 3), "Labor Day (Day 2)"))
        elif labor_day.weekday() == SUN:
            days.append((date(year, 5, 2), "Labor Day"))
            days.append((date(year, 5, 3), "Labor Day (Day 2)"))
        else:
            days.append((labor_day, "Labor Day"))
            days.append((date(year, 5, 2), "Labor Day (Day 2)"))
        return days
