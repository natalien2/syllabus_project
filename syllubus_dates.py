import calendar

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# class Calendar is already created
my_calendar = calendar.Calendar()

# get year and month
# year = 2022
# start_mon = 8
# start_day = 29
# count = 0


def print_dates(year, start_month, end_month, start_day=0, end_day=0):
    results = ""
    current_month = start_month
    # iterate over the months
    while current_month <= end_month:
        # iterate through the days
        for day in my_calendar.itermonthdays2(year, current_month):
            date = day[0]
            day_of_week = day[1]

            # If the day corresponds to the previous or the month after
            if date == 0:  # and day in HOLIDAY:
                continue

            if day_of_week not in [MONDAY, TUESDAY, WEDNESDAY, THURSDAY]:
                continue

            print_format = str(current_month) + "/" + str(date) + ", "

            if current_month == start_month:
                if date >= start_day:
                    results += print_format
            elif current_month == end_month:
                if date <= end_day:
                    results += print_format
            else:
                results += print_format
        current_month += 1
    return results


result = print_dates(year=2022, start_month=8, end_month=12, start_day=29, end_day=12)
# print(result)
