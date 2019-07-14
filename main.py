import calendar


def get_leap_years(start: int, stop: int):
    if start > stop:
        start, stop = stop, start
    leap_years = filter(lambda x: calendar.isleap(x), range(start, stop, +1))
    return list(leap_years)


print(get_leap_years(2019, 2018))
