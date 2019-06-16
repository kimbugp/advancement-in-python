#!/bin/python3

import math
import os
import random
import re
import sys


def factors(x):
    l = list()
    for i in range(1, x + 1):
        if x % i == 0:
            l.append(i)
    return l


# for _ in range(5):
#     x = int(input())
#     print(factors(x))


def connectedCities(n, g, originCities, destinationCities):
    """Get connected cities
    
    Args:
        n (int ): number of cities
        g (int): threshold value 
        originCities (list): [description]
        destinationCities (list): [description]
    """
    result = list()
    for origin, destination in zip(originCities, destinationCities):
        divisor = math.gcd(origin, destination)
        if divisor > g:
            result.append(1)
            print("Valid route", origin, destination, sep=" ")
        else:
            print("InValid route", origin, destination, sep=" ")
            result.append(0)
    return result


connectedCities(6, 0, [1, 2, 4, 6], [3, 3, 3, 4])
# connectedCities(6, 2, [4, 2, 9], [8, 5, 6])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Number of cities ").strip())

    g = int(input("Threshold ").strip())

    originCities_count = int(input("Origin Cities count ").strip())

    originCities = []

    for _ in range(originCities_count):
        originCities_item = int(input().strip())
        originCities.append(originCities_item)

    destinationCities_count = int(input("Destination city count ").strip())

    destinationCities = []

    for _ in range(destinationCities_count):
        destinationCities_item = int(input().strip())
        destinationCities.append(destinationCities_item)

    result = connectedCities(n, g, originCities, destinationCities)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
