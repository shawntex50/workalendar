from datetime import date

from workalendar.asia import India

cal = India()
for i in cal.holidays(2024):
    print(i)
print(cal.FIXED_HOLIDAYS)

