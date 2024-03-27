from datetime import date

from workalendar.europe import Ireland

cal = Ireland()
for i in cal.holidays(2024):
    print(i)
#print(cal.holidays(2020))
#print(cal.is_working_day(date(2024, 2, 14)))
print(cal.get_st_brigids_day(2023))
print(cal.is_working_day(date(2023, 2, 6)))
print(cal.get_st_brigids_day(2024))
print(cal.is_working_day(date(2024, 2, 5)))
print(cal.get_st_brigids_day(2025))
print(cal.is_working_day(date(2025, 2, 3)))
print(cal.get_st_brigids_day(2020))
print(cal.is_working_day(date(2020, 2, 3)))

# print(cal.FIXED_HOLIDAYS)

