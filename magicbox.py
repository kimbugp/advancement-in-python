from functools import reduce
from itertools import combinations, permutations


def formingMagicSquare(square):
    possible = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    final = []

    for p in possible:
        partial = 0
        for index, item in enumerate(square):
            res = sum(map(lambda x, y: abs(x - y), p[index], item))
            partial += res
        final.append(partial)
    return min(final)


formingMagicSquare([[4, 5, 8], [2, 4, 1], [1, 9, 7]])
