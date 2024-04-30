from ..core import IslamicCalendar
from ..registry_tools import iso_register

@iso_register('IN')
class India(IslamicCalendar):
    "India"

    include_new_years_day = False

    FIXED_HOLIDAYS = (
        (1, 26, "Republic Day"),
        (8, 15, "Independence Day"),
        (10, 2, "Gandhi Jayanti"),
        (1, 1, "New Year's Day"),
        (1, 14, "Makar Sankranti / Pongal"),
        (1, 26, "Republic Day"),
        (5, 1, "Labour Day / May Day"),
        (8, 15, "Independence Day"),
        (10, 2, "Gandhi Jayanti"),
        (10, 26, "Diwali"),
        (12, 25, "Christmas"),
    )

    include_start_ramadan = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 4
    include_eid_al_adha = True
    length_eid_al_adha = 4
