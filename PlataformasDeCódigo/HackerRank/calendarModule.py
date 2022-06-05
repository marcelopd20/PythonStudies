import calendar
m ,d, y = (int(x) for x in input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())