import array

from collections import Counter


class Piles():

    piles = []
    player = 0

    def __init__(self, piles):
        self.piles = array.array('i', piles)

    def remove(self, column, value):
        self.piles[column] -= value
        self.player = 1 - self.player
        return self.piles

    def max(self):
        return max(self.piles)

    def __repr__(self):
        return str(self.piles)


def validate_input(piles, k):
    if not 1 <= len(piles) <= 1000:
        raise ValueError("Piles must be less than 1000")
    if not 1 <= max(piles) <= 100000:
        raise ValueError("Piles values must be less than 100000")

    if not 1 <= k <= 1000:
        raise ValueError("k must be less than 1000")


def gameOfPiles(piles, k):
    validate_input(piles, k)
    players = ['Alex', 'Sam']
    piles = Piles(piles)
    while piles.max() >= k:
        multiples = list(range(0, piles.max() + 1, k))
        index = piles.piles.index(piles.max())
        piles.remove(index, multiples[-1])
        print("====>", piles.max(), "==>", piles, "===>", multiples)
    while set(piles.piles) != {0}:
        index = piles.piles.index(piles.max())
        piles.remove(index, 1)

    winner = players[piles.player]
    return f"{winner} wins the game of {len(piles.piles)} pile(s)."


def stonePiles(arr):
    total = 0
    # Get total occurrence of each item in array
    counter = Counter(arr)

    # End Numbers
    # generate a list of 50 items 
    end_numbers = [0, 1]
    while len(end_numbers) <= 50:
        # Add the product of last item of end numbers
        # and the length of end numbers
        end_numbers += [end_numbers[-1] + 1] * len(end_numbers)

    # sizes of piles that lead to loss
    losing_numbers = [1, 2, 4, 8]

    # Check if the nimber number theorem is satisfied
    # For the 1 index user win, the XOR(n1,n2,n3,) should be equal 0
    # else 1 index user
    for size, count in counter.items():
        if size not in losing_numbers and count & 1 != 0:
            total ^= (size - min(4, end_numbers[size]))
    return ('ALICE' if total != 0 else 'BOB')


print(stonePiles([2, 30, 40, 60, 10, 10, 10]))
