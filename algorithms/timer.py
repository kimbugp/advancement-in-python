import time


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        stop = time.time()
        name = method.__name__.upper()
        timed = stop - start
        return result, timed

    return timed
    