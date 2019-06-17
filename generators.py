def check_prime(x):
    if x >= 2:
        for n in range(2, x):
            if (x % n) == 0:
                return False
        return True
    else:
        return False


def manipulate_generator(generator, n):
    n += 1

    if n == 2:
        next(generator)
        next(generator)

    elif check_prime(n):
        next(generator)


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = 10
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
