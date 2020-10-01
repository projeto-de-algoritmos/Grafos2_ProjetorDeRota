import math

class Graph(object):

    def __init__(self, graph_dict={}):
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, *edge, bidirectional=True):
        (vertex1, vertex2, cost) = edge
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.__add_edge_no_repetition(vertex1, vertex2, cost)
        if bidirectional:
            self.__add_edge_no_repetition(vertex2, vertex1, cost)

    def direct_cost(self, vertex1, vertex2):
        list_v1 = self.__graph_dict[vertex1]
        for (v, cost) in list_v1:
            if v == vertex2:
                return cost
        else:
            return math.inf

    def __add_edge_no_repetition(self, v1, v2, cost):
        list_v1 = self.__graph_dict[v1]
        for i, (v, _) in enumerate(list_v1):
            if v == v2:
                list_v1[i] = (v2, cost)
                break
        else:
            list_v1.append((v2, cost))

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for (neighbour, cost) in self.__graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour, cost))
        return edges

    def __str__(self):
        return 'Vertices: {0}\nEdges: {1}'.format(sorted(self.vertices()), sorted(self.edges()))

