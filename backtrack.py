def subset(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[(i + 1):]
        yield from subset(remaining, target, partial + [n], partial_sum + n)