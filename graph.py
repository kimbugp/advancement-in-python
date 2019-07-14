from collections import defaultdict


class Graph(object):
    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = defaultdict(set)
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def addEdge(self, u, v):
        self.__graph_dict[u].add(v)

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def find_path(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_shortest_path(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None

        shortest = None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_shortest_path(
                    vertex, end_vertex, path)
                if extended_path:
                    if not shortest or len(extended_path) < len(shortest):
                        shortest = extended_path
        return shortest

    def __repr__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res