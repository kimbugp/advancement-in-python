from functools import reduce
from itertools import combinations, permutations


def formingMagicSquare(square):
    K = 15
    n = 3
    pivot = 5
    center = [1, 5, 9, 3, 7]
    sample = list(combinations(range(1, n**2 + 1), n))
    # sample = list(permutations(range(1, n**2 + 1), n))
    possible = list(
        filter(
            lambda x: sum(x) == K and x[n // 2] in center and x[0] != pivot and
            x[-1] != pivot, sample))
    import pdb; pdb.set_trace()
    center_pieces = list(filter(lambda x: x[n // 2] == pivot, possible))
    for _ in center_pieces:
        possible.remove(_)
    # remove losing centers
    center_pieces = list(
        filter(lambda x: x[0] not in [2, 4, 6, 8] or x[-1] not in [2, 4, 6, 8],
               center_pieces))

    tries = []
    for center_piece in center_pieces:
        import pdb
        pdb.set_trace()

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
