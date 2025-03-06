from abc import ABC, abstractmethod


class WeightedGraphInterface(ABC):
    """"""
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        """"""
        super().__init__()

    @abstractmethod
    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """"""
        pass

    @abstractmethod
    def is_adjacent(self, vertex1: int, vertex2: int) -> bool:
        """"""
        pass

    @abstractmethod
    def return_adjacent(self, vertex: int) -> list[tuple[int, int]]:
        """"""
        pass

    @abstractmethod
    def get_path_weight(self, *path) -> int:
        """Traverse a path and calculates total weight.

        Returns:
            int: -1 if there is no such a path in graph,
                 total weight of path otherwise.
        """
        pass


class WeightedGraph(WeightedGraphInterface):
    def __init__(self, num_vertices: int) -> None:
        super().__init__(num_vertices)
        self.graph = {i: [] for i in range(1, num_vertices + 1)}
        self.missing_vertices = []

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Sets a weighted edge between vertex1 and vertex2.

        Raises:
            KeyError: if vertex1 or vertex2 are not in the graph.
        """
        try:
            self.missing_vertices = []
            if vertex1 not in self.graph:
                self.missing_vertices.append(vertex1)
            if vertex2 not in self.graph:
                self.missing_vertices.append(vertex2)
            if self.missing_vertices:
                missing_vertices_repr = ', '.join(map(str, self.missing_vertices))
                raise KeyError(f"There {'is' if len(self.missing_vertices) == 1 else 'are'} no {missing_vertices_repr} "
                               f"vert{'ex' if len(self.missing_vertices) == 1 else 'ices'} "
                               f"in the graph with {len(self.graph)} vertices.")
        except KeyError as e:
            print(str(e))
            return

        existing_edge = next((edge for edge in self.graph[vertex1] if edge[0] == vertex2), None)
        if existing_edge:
            self.graph[vertex1].remove(existing_edge)
            self.graph[vertex2].remove((vertex1, existing_edge[1]))

        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def is_adjacent(self, vertex1: int, vertex2: int) -> bool:
        """Checks that vertex2 is adjacent to vertex1.

        Returns:
            bool: True if vertex2 is adjacent to vertex1, False otherwise.

        Raises:
            KeyError: if vertex1 or vertex2 is not in the graph.
        """
        return any(neighbour == vertex2 for neighbour, _ in self.graph.get(vertex1, []))

    def return_adjacent(self, vertex: int) -> list[tuple[int, int]]:
        """Returns all adjacent vertices to the given vertex.

        Returns:
            list[tuple[int, int]]: adjacent vertices with their weight to vertex.

        Raises:
            KeyError: if the given vertex is not in the graph.
        """
        return self.graph[vertex]

    def get_path_weight(self, *path) -> int:
        """"""
        pass


if __name__ == "__main__":
    """> 5      # Total num of vertices
       > 2      # Num of edges to add
       > 1 2 15 # 1st
       > 2 3 13 # 2nd
       > 1 2 3  # Path
       28
    """
    # get Total num of vertices
    graph = WeightedGraph(5)
    print(graph.return_adjacent(2))
    graph.add_edge(2, 3, 20)
    graph.add_edge(2, 3, 30)
    print(graph.return_adjacent(2))
    print(graph.return_adjacent(3))
    graph.add_edge(2, 6, 7)
    graph.add_edge(7, 6, 7)

    # get Num of edges to add
    # loop through input edges

    # get a path

    # return total weight of the path
