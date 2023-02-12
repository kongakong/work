from datetime import date, datetime, timedelta
import pytz
from icalendar import Calendar, Event


pub_2022_raw_data = [
("New Year's Day",    "Sunday", "1 January"),
("Additional Day",    "Tuesday", "3 January"),
("Australia Day",    "Thursday", "26 January"),
("Good Friday",    "Saturday", "15 April"),
("Easter Saturday - the Saturday following Good Friday","Sunday", "16 April"),
("Easter Sunday",    "Monday", "17 April"),
("Easter Monday",    "Tuesday", "18 April"),
("Anzac Day",    "Tuesday", "25 April"),
("King's Birthday",    "Tuesday", "13 June"),
("1 Bank Holiday",    "Tuesday", "1 August"),
("National Day of Mourning",    "Friday", "22 September"),
("Labour Day",    "Tuesday", "3 October"),
("Christmas Day public holiday",    "Monday", "25 December"),
("Additional Day",    "Wednesday", "27 December"),
("Boxing Day",    "Tuesday", "26 December"),
]

date_format = "%d %B %Y"
pub_2022 = [datetime.strptime(date_string + " 2022", date_format) for (_, _, date_string) in pub_2022_raw_data]
print(pub_2022)

def all_mondays(start, end):
    monday = timedelta(days=-6)
    d = start
    while d <= end:
        if d.weekday() == 0:
            yield d
        d += timedelta(days=1)

start_date = datetime(2021, 1, 1, 0, 0)
end_date = datetime(2022, 12, 31, 0, 0)
mondays = list(all_mondays(start_date, end_date))

cal = Calendar()
for monday in mondays:
    if monday in pub_2022: 
        print("%s is a public holiday" % monday)
    else:
        event = Event()
        event.add('summary', 'WFH Monday')
        event.add('dtstart', monday)
        event.add('dtend', monday + timedelta(days=1))
        event.add('dtstamp', monday)
        cal.add_component(event)

with open('mondays.ics', 'wb') as f:
    f.write(cal.to_ical())
