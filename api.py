import datetime
import json
import urllib.request
import time
from urllib.error import URLError


def data_filter(firstDate, lastDate, weekDay):
    """
    Filters data in a given date range by the day of the week
    
    Args:
        firstDate (datetime):  start date range
        lastDate (datetime): end date range
        weekDay (datetime): weekday to search by
    
    Returns:
        boolean: true of false if data value falls on a given day
    """

    def my_filter(data):
        raw_day = data.get("date")
        day = datetime.datetime.strptime(raw_day, '%d-%B-%Y')
        week_day = datetime.datetime.weekday(day)
        if firstDate <= day <= lastDate and week_day == weekDay:
            return True
        return False

    return my_filter


def openAndClosePrices(firstDate, lastDate, weekDay):
    url = "https://jsonmock.hackerrank.com/api/stocks?page={0}"
    try:
        firstDate, lastDate = map(
            lambda x: datetime.datetime.strptime(x, '%d-%B-%Y'),
            [firstDate, lastDate])
        weekDay = time.strptime(weekDay, "%A").tm_wday
    except ValueError:
        raise ValueError("Enter date in the format dd-MM-YY ie 15-August-2001")

    iterator = get_data(url)
    for item in iterator:
        filter1 = data_filter(firstDate, lastDate, weekDay)
        response = list(filter(filter1, item.get("data")))
        print(item.get('page'))
        for no, value in enumerate(response):
            print(no + 1,
                  value['date'],
                  value['open'],
                  value['close'],
                  sep=" ")


def get_data(url):
    n = 1
    data = json.load(urllib.request.urlopen(url.format(1)))
    pages = data.get("total_pages")
    yield data
    while n < pages:
        try:
            yield json.load(urllib.request.urlopen(url.format(n + 1)))
        except URLError:
            raise URLError("Check your connection")
        n += 1


try:
    _firstDate = '26-March-2001'
except:
    _firstDate = None

try:
    _lastDate = "15-August-2019"
except:
    _lastDate = None

try:
    _weekDay = "Wednesday"
except:
    _weekDay = None

openAndClosePrices(_firstDate, _lastDate, _weekDay)
