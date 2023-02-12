from datetime import date, timedelta

def all_mondays(start, end):
    monday = timedelta(days=-6)
    d = start
    while d <= end:
        if d.weekday() == 0:
            yield d
        d += timedelta(days=1)

start_date = date(2021, 7, 1)
end_date = date(2022, 6, 30)
mondays = list(all_mondays(start_date, end_date))

print(mondays)

