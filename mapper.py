import math
from collections import defaultdict


def addEdge(graph, u, v):
    graph[u].add(v)


def find_path(graph, start, end):
    for path in graph[start]:
        if end in graph[path]:
            return True
    return False


def connectedCities(n, g, originCities, destinationCities):
    """Get connected cities
    
    Args:
        n (int ): number of cities
        g (int): threshold value 
        originCities (list): [description]
        destinationCities (list): [description]
    """
    graph = defaultdict(set)
    all_cities = originCities + destinationCities

    for city in all_cities:
        for destination in all_cities:
            divisor = math.gcd(city, destination)
            if divisor > g:
                addEdge(graph, city, destination)
    result = list()
    for origin, destination in zip(originCities, destinationCities):
        path = find_path(graph, origin, destination)
        print(origin, '  ', destination)
        if path:
            result.append(1)
        else:
            result.append(0)
    print(result)
    return result


connectedCities(10, 1, [10, 4, 3, 6], [3, 6, 2, 9])