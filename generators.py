def check_prime(x):
    if x >= 2:
        for n in range(2, x - 1):
            if (x % n) == 0:
                return False
        return True
    else:
        return False


def manipulate_generator(generator, n):
    if check_prime(n):
        generator.send(None)

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
