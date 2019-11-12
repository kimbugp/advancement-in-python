def reverse(var):
    def divide(var):
        if len(var) == 0:
            return var
        else:
            return divide(var[1:]) + var[0]

    length = len(var) // 2
    return divide(var[length::]) + divide(var[0:length])


def reverse_v2(var):
    var = list(var)
    length = len(var)
    tracker = 0
    for index in range(length // 2):
        var[index], var[length - tracker - 1] = var[length - tracker -
                                                    1], var[index]
        tracker += 1
    return ''.join(var)


def palindrome(var):
    if len(var) <= 1:
        return True
    if var[0] == var[-1]:
        return palindrome(var[1:-1])
    return False


def rev(var):
    if len(var) <= 1:
        return var
    last = var[-1]
    first = var[0]
    return last + rev(var[1:-1]) + first


items = {}


def fibonacci(number, recursive=False):
    def iterative(number):
        start = 1
        total = 1
        prev1 = 0
        prev2 = 0
        while start < number:
            if number not in items:
                prev2 = prev1
                prev1 = total
                total = prev1 + prev2
                start += 1
                items[start] = total

        return total

    def recurse(number):
        if number <= 2:
            return 1
        if number not in items:
            items[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return items[number]

    def solve(x):
        return recurse(number) if x else iterative(number)

    return solve(recursive)


x = fibonacci(10)
