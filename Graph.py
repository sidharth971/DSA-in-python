"""
@Sidharth Sahoo
A graph is a non-linear data structure, different from linear ones like arrays and linked lists.
Trees are a special case of graphs, as they do not form cycles, whereas graphs can have cycles.
"""
from cloudinit.net.renderers import search


class GraphUsingAdjacencyMatrix:
    def __init__(self, vno: int) -> None:
        self.vertex_count = vno
        self.adj_matrix = [[0] * vno for _ in range(vno)]

    def __update_vertex(self, u: int, v: int, weight: int) -> None:
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print('Invalid vertex')

    def add_ranges(self, u: int, v: int, weight: int = 1) -> None:
        self.__update_vertex(u, v, weight)

    def remove_vertex(self, u: int, v: int) -> None:
        self.__update_vertex(u, v, 0)

    def has_edges(self, u: int, v: int) -> int:
        return self.adj_matrix[u][v] != 0

    def print_vertex(self) -> None:
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))


gf = GraphUsingAdjacencyMatrix(5)
gf.add_ranges(0, 1)
gf.add_ranges(1, 2)
gf.add_ranges(2, 3)
gf.add_ranges(3, 4)
gf.add_ranges(2, 4)

print(gf.has_edges(0, 3))
print(gf.has_edges(2, 4))
gf.print_vertex()
gf.remove_vertex(2, 4)


class GraphUsingadjAcencyList:
    def __init__(self, vno: int) -> None:
        self.vertexes_count = vno
        self.adjecency_list = {v: [] for v in range(vno)}
    def __update_adjacency(self, u: int, v: int, weight: int) -> None:
        if 0 <= u < self.vertexes_count and 0 <= v < self.vertexes_count:
            self.adjecency_list[u].append((v, weight))
            self.adjecency_list[v].append((u, weight))
        else:
            print('Invalid Vertexes')
    def add_edges(self, u: int, v: int, weight: int=1) -> None:
        self.__update_adjacency(u, v, weight)

    def remove_vertexes(self, u: int, v: int) -> None:
        if 0 <= u < self.vertexes_count and 0 <= v < self.vertexes_count:
            self.adjecency_list[u] = list(filter(lambda x: x[0] != v, self.adjecency_list[u]))
            self.adjecency_list[v] = list(filter(lambda x: x[0] != u , self.adjecency_list[v]))
        else:
            print('Invalid Vertexes')

    def has_edeges(self, u: int, v: int) -> bool:
        return any(vert == v for vert, _ in self.adjecency_list[u])

    def print_edeses(self):
        for k, v in self.adjecency_list.items():
            print(k, v)



adc_lst = GraphUsingadjAcencyList(5)
adc_lst.add_edges(0,1)
adc_lst.add_edges(1,2)
adc_lst.add_edges(2,3)
adc_lst.add_edges(3,4)
adc_lst.add_edges(1,3)

print(adc_lst.has_edeges(0, 3))
print(adc_lst.has_edeges(3, 4))
adc_lst.print_edeses()







