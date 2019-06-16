import datetime
import json
import urllib.request
import time


def data_filter(firstDate, lastDate, weekDay):
    def myfilter(data):
        day = data.get("date")
        day = datetime.datetime.strptime(day, '%d-%B-%Y')
        week_day = datetime.datetime.weekday(day)
        if firstDate <= day <= lastDate and week_day == weekDay:
            return True
        return False

    return myfilter


def openAndClosePrices(firstDate, lastDate, weekDay):
    url = "https://jsonmock.hackerrank.com/api/stocks?page={0}"
    try:
        firstDate, lastDate = map(
            lambda x: datetime.datetime.strptime(x, '%d-%B-%Y'),
            [firstDate, lastDate])
        weekDay = time.strptime(weekDay, "%A").tm_wday
    except ValueError:
        raise ValueError("Enter date in the format dd-MM-YY ie 15-August-2001")

    data = json.load(urllib.request.urlopen(url.format(1)))
    pages = data.get("total_pages")
    iterator = get_data(url, pages)
    for page in range(pages):
        data = next(iterator)
        filter1 = data_filter(firstDate, lastDate, weekDay)
        response = list(filter(filter1, data.get("data")))
        for value in response:
            print(value['date'], value['open'], value['close'], sep=" ")


def get_data(url, pages):
    n = 1
    while n <= pages:
        yield json.load(urllib.request.urlopen(url.format(n)))
        n += 1


try:
    _firstDate = '26-March-2001'
except:
    _firstDate = None

try:
    _lastDate = "15-August-2001"
except:
    _lastDate = None

try:
    _weekDay = "Wednesday"
except:
    _weekDay = None

openAndClosePrices(_firstDate, _lastDate, _weekDay)