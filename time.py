import time
import calendar
import pandas as pd
methods = {
    "lambda":
    lambda start, stop: filter(lambda x: calendar.isleap(x),
                               range(start, stop, +1)),
    "comprehesion":
    lambda start, stop:
    [x for x in range(start, stop, +1) if calendar.isleap(x)]
}


def get_leap_years(start: int, stop: int, method):
    if start > stop:
        start, stop = stop, start
    leap_years = method(start, stop)
    return list(leap_years)


x = pd.DataFrame(None, columns=methods.keys())
for _ in range(1000):
    y = {}
    for key, method in methods.items():
        start = time.time()
        get_leap_years(1, 2100, method)
        end = time.time()
        y[key] = end - start
    x = x.append(y, True)

print(x.mean())
