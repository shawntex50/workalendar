from datetime import date

from ..core import Calendar, MON, SAT, SUN
from ..astronomy import calculate_equinoxes
from ..registry_tools import iso_register


@iso_register('JP')
class Japan(Calendar):
    "Japan"

    # Japan uses the "western" workweek
    WEEKEND_DAYS = (SAT, SUN)

    FIXED_HOLIDAYS = Calendar.FIXED_HOLIDAYS + (
        (2, 11, "Foundation Day"),
        (4, 29, "Showa Day"),
        (5, 3, "Constitution Memorial Day"),
        (5, 4, "Greenery Day"),
        (5, 5, "Children's Day"),
        (11, 3, "Culture Day"),
        (11, 23, "Labour Thanksgiving Day"),
    )

    def get_fixed_holidays(self, year):
        """
        Fixed holidays for Japan.
        """
        days = super().get_fixed_holidays(year)
        # Some Holidays in Japan are observed the following day,
        # if the holiday falls on a Sunday
        if year >= 2016 and year != 2021:
            # days.append((date(year, 8, 11), "Mountain Day"))
            mountain_day = date(year, 8, 11)
            days.append((mountain_day, "Mountain Day"))
            if mountain_day.weekday() == SUN:
                days.append((date(year, 8, 12), "Mountain Day Observed"))

        new_years_day = date(year, 1, 1)
        if new_years_day.weekday() == SUN:
            days.append((date(year, 1, 2), "New Years Day Observed"))

        childrens_day = date(year, 5, 5)
        if childrens_day.weekday() == SUN:
            days.append((date(year, 5, 6), "Children's Day Observed"))

        foundation_day = date(year, 2, 11)
        if foundation_day.weekday() == SUN:
            days.append((date(year, 2, 12), "Foundation Day Observed"))

        culture_day = date(year, 11, 3)
        if culture_day.weekday() == SUN:
            days.append((date(year, 11, 4), "Culture Day Observed"))

        showa_day = date(year, 4, 29)
        if showa_day.weekday() == SUN:
            days.append((date(year, 4, 30), "Showa Day Observed"))

        constitution_day = date(year, 5, 3)
        if constitution_day.weekday() == SUN:
            days.append((date(year, 5, 6), "Constitution Memorial Day Observed"))

        greenery_day = date(year, 5, 4)
        if greenery_day.weekday() == SUN:
            days.append((date(year, 5, 6), "Greenery Day Observed"))

        labour_day = date(year, 11, 23)
        if labour_day.weekday() == SUN:
            days.append((date(year, 11, 24), "Labour Thanksgiving Day Observed"))

        # Change in Emperor
        if year < 2019:
            emperors_birthday = date(year, 12, 23), "The Emperor's Birthday"
            days.append((emperors_birthday, "The Emperor's Birthday"))
            if emperors_birthday.weekday() == SUN:
                days.append((date(year, 12, 24), "The Emperor's Birthday Observed"))
        if year > 2019:
            emperors_birthday = date(year, 2, 23)
            days.append((emperors_birthday, "The Emperor's Birthday"))
            if emperors_birthday.weekday() == SUN:
                days.append((date(year, 2, 24), "The Emperor's Birthday Observed"))
        # Lots of adjustments for new emperor
        if year == 2019:
            days.extend([
                (date(year, 4, 30), "Coronation Day"),
                (date(year, 5, 1), "Coronation Day"),
                (date(year, 5, 2), "Coronation Day"),
                (date(year, 10, 22), "Enthronement Ceremony Day"),
                (date(year, 11, 4), "Culture Day Observed"),
            ])
        if year == 2020:
            days.extend([
                (date(year, 2, 24), "The Emperor's Birthday Observed"),
                (date(year, 5, 6), "Constitution Memorial Day Observed"),
                (date(year, 8, 10), "Mountain Day"),
            ])
            # Mountain Day is 8/10 this year for some reason
            # The next year that will be different is 2024
            days.remove((date(year, 8, 11), "Mountain Day"))
        if year == 2021:
            # Mountain Day is changed due to Tokyo's Olympics
            days.extend([
                (date(year, 8, 8), "Mountain Day"),
                (date(year, 8, 9), "Mountain Day Observed"),
            ])
        return days

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)
        equinoxes = calculate_equinoxes(year, 'Asia/Tokyo')
        coming_of_age_day = Japan.get_nth_weekday_in_month(year, 1, MON, 2)
        respect_for_the_aged = Japan.get_nth_weekday_in_month(year, 9, MON, 3)

        if year == 2020:
            # Health and Sports Day will continue on the 2nd monday
            # of October, except in 2020 when it will happen in July
            # https://www.timeanddate.com/holidays/japan/sports-day
            marine_day = date(2020, 7, 23)
            health_and_sport = date(2020, 7, 24)
        elif year == 2021:
            # Marine Day & Sport's Day are changed due to Tokyo's Olympics
            marine_day = date(year, 7, 22)
            health_and_sport = date(year, 7, 23)
        else:
            # Marine Day is on a Thursday in 2020 for some year
            # https://www.timeanddate.com/holidays/japan/sea-day
            marine_day = Japan.get_nth_weekday_in_month(year, 7, MON, 3)
            health_and_sport = Japan.get_nth_weekday_in_month(year, 10, MON, 2)

        # Health and Sports Day became "Sports Day" as of 2020
        if year < 2020:
            health_and_sport_label = "Health and Sports Day"
        else:
            health_and_sport_label = "Sports Day"

        vernal_equinox = equinoxes[0]
        if vernal_equinox.weekday() == SUN:
            days.append((self.find_following_working_day(vernal_equinox), "Vernal Equinox Observed"))

        autumnal_equinox = equinoxes[1]
        if autumnal_equinox.weekday() == SUN:
            days.append((self.find_following_working_day(autumnal_equinox), "Autumnal Equinox Observed"))

        days.extend([
            (coming_of_age_day, 'Coming of Age Day'),
            (marine_day, "Marine Day"),
            (equinoxes[0], "Vernal Equinox Day"),
            (respect_for_the_aged, "Respect-for-the-Aged Day"),
            (equinoxes[1], "Autumnal Equinox Day"),
            (health_and_sport, health_and_sport_label),
        ])

        return days


class JapanBank(Japan):
    """The Bank of Japan is closed additional days other than
    national holidays.
    https://www.boj.or.jp/en/about/outline/holi.htm/
    """

    FIXED_HOLIDAYS = Japan.FIXED_HOLIDAYS + (
        (1, 2, "New Year Bank Holiday"),
        (1, 3, "New Year Bank Holiday"),
        (12, 31, "New Year Bank Holiday"),
    )
