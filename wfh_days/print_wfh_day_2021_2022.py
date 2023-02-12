from datetime import date, datetime, timedelta
import pytz
from icalendar import Calendar, Event


pub_2022_raw_data = [
    ("New Year's Day", "Sunday", "1 January"),
    ("Additional Day", "Tuesday", "3 January"),
    ("Australia Day", "Thursday", "26 January"),
    ("Good Friday", "Saturday", "15 April"),
    ("Easter Saturday - the Saturday following Good Friday", "Sunday", "16 April"),
    ("Easter Sunday", "Monday", "17 April"),
    ("Easter Monday", "Tuesday", "18 April"),
    ("Anzac Day", "Tuesday", "25 April"),
    ("King's Birthday", "Tuesday", "13 June"),
    ("1 Bank Holiday", "Tuesday", "1 August"),
    ("National Day of Mourning", "Friday", "22 September"),
    ("Labour Day", "Tuesday", "3 October"),
    ("Christmas Day public holiday", "Monday", "25 December"),
    ("Additional Day", "Wednesday", "27 December"),
    ("Boxing Day", "Tuesday", "26 December"),
]

pub_2021_raw_data = [
    ("New Year's Day", "Sunday", "1 January"),
    ("Australia Day", "Thursday", "26 January"),
    ("Good Friday	", "Friday", "2 April"),
    ("Easter Saturday - the Saturday following Good Friday	", "Saturday", "3 April"),
    ("Easter Sunday", "Sunday", "4 April"),
    ("Easter Monday", "Monday,", "5 April"),
    ("Anzac Day", "Tuesday,", "25 April"),
    ("King's Birthday	", "Monday", "14 June"),
    ("Bank Holiday	", "Monday", "2 August"),
    ("Labour Day	", "Monday", "4 October"),
    ("Christmas Day public holiday	", "Monday", "25 December"),
    ("Boxing Day	", "Tuesday", "26 December"),
]

pub_2023_raw_data = [
    ("New Year's Day", "Sunday", "1 January"),
    ("Additional Day", "Monday", "2 January"),
    ("Australia Day", "Thursday", "26 January"),
    ("Good Friday	", "Friday", "7 April"),
    ("Easter Saturday - the Saturday following Good Friday	", "Saturday", "8 April"),
    ("Easter Sunday", "Sunday", "9 April"),
    ("Easter Monday", "Monday,", "10 April"),
    ("Anzac Day", "Tuesday,", "25 April"),
    ("King's Birthday	", "Monday", "12 June"),
    ("Bank Holiday	", "Monday", "7 August"),
    ("Labour Day	", "Monday", "2 October"),
    ("Christmas Day public holiday	", "Monday", "25 December"),
    ("Boxing Day	", "Tuesday", "26 December"),
]
date_format = "%d %B %Y"
pub_2021 = [
    datetime.strptime(date_string + " 2021", date_format)
    for (_, _, date_string) in pub_2021_raw_data
]
pub_2022 = [
    datetime.strptime(date_string + " 2022", date_format)
    for (_, _, date_string) in pub_2022_raw_data
]
pub_2023 = [
    datetime.strptime(date_string + " 2023", date_format)
    for (_, _, date_string) in pub_2023_raw_data
]


def all_mondays(start, end):
    monday = timedelta(days=-6)
    d = start
    while d <= end:
        if d.weekday() == 0:
            yield d
        d += timedelta(days=1)


start_date = datetime(2021, 7, 1, 0, 0)
end_date = datetime(2022, 6, 30, 0, 0)
mondays = list(all_mondays(start_date, end_date))

all_holidays = pub_2021 + pub_2022
print(all_holidays)

cal = Calendar()
for monday in mondays:
    if monday in all_holidays:
        #    print("%s is a public holiday" % monday)
        pass
    else:
        print("%s" % monday.date())
        event = Event()
        event.add("summary", "WFH Monday")
        event.add("dtstart", monday)
        event.add("dtend", monday + timedelta(days=1))
        event.add("dtstamp", monday)
        cal.add_component(event)

with open("mondays.ics", "wb") as f:
    f.write(cal.to_ical())
