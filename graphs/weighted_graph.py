from abc import ABC, abstractmethod


class WeightedGraphInterface(ABC):
    """Represents an abstract class that defines an interface weighted graph."""
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        """Initializes the weighted graph with finite given number of vertices.

        Args:
            num_vertices (int): The given number of vertices.
        """
        super().__init__()

    @abstractmethod
    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Sets an undirected weighted edge between two given vertices.

        Args:
            vertex1 (int): The first given vertex.
            vertex2 (int): The second given vertex.
            weight (int): The weight of the edge.
        """
        pass

    @abstractmethod
    def is_adjacent(self, vertex1: int, vertex2: int) -> bool:
        """Checks if the given vertex2 is adjacent to the given vertex1.

        Args:
            vertex1 (int): The first given vertex.
            vertex2 (int): The second given vertex.
        """
        pass

    @abstractmethod
    def return_adjacent(self, vertex: int) -> list[tuple[int, int]]:
        """Returns adjacent vertices to the given vertex.

        Args:
            vertex (int): The given vertex.
        """
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
    """Represents weighted graph."""
    def __init__(self, num_vertices: int) -> None:
        """Initializes weighted graph with finite given number of vertices."""
        super().__init__(num_vertices)
        self.graph: dict = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Sets an undirected weighted edge between vertex1 and vertex2.

        The method sets a new undirected weighted edge and removes an old edge from the graph
        if between given vertices is already edge.

        Args:
            vertex1 (int): The first given vertex.
            vertex2 (int): The second given vertex.
            weight (int): The weight of the edge between vertex1 and vertex2.

        Returns:
            None: If the vertex1 or the vertex2 is not in the graph.
        """
        try:
            self.check_miss_vert(vertex1, vertex2)
        except KeyError as e:
            # raise Exception(f"{vertex1} or {vertex2} does not exist in the graph.") from e
            print(str(e))
            return

        existing_edge = next((edge for edge in self.graph[vertex1] if edge[0] == vertex2), None)
        if existing_edge:
            self.graph[vertex1].remove(existing_edge)
            self.graph[vertex2].remove((vertex1, existing_edge[1]))

        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def is_adjacent(self, vertex1: int, vertex2: int) -> bool | None:
        """Checks that vertex2 is adjacent to vertex1.

        Args:
            vertex1 (int): The first given vertex.
            vertex2 (int): The second given vertex.

        Returns:
            bool: True if vertex2 is adjacent to vertex1, False otherwise.
            None: If the vertex1 or vertex2 is not in the graph.
        """
        try:
            self.check_miss_vert(vertex1, vertex2)
        except KeyError as e:
            # raise Exception(f"{vertex1} or {vertex2} does not exist in the graph.") from e
            print(str(e))
            return

        return any(neighbour == vertex2 for neighbour, _ in self.graph.get(vertex1, []))

    def return_adjacent(self, vertex: int) -> list[tuple[int, int]] | None:
        """Returns all adjacent vertices to the given vertex.

        Args:
            vertex (int): The given vertex to get the adjacent vertices from it.

        Returns:
            list[tuple[int, int]]: Adjacent vertices with their weight to vertex.
            None: If the given vertex is not in the graph.
        """
        try:
            self.check_miss_vert(vertex)
        except KeyError as e:
            # raise Exception(f"{vertex} does not exist in the graph.") from e
            print(str(e))
            return

        return self.graph[vertex]

    def get_path_weight(self, *path: int) -> int | None:
        """Calculates the total weight of a given path in the graph.

        The method traverses the given sequence of vertices and sums up the weights
        of the edges connecting consecutive vertices in the path. If at any point
        an edge does not exist between two consecutive vertices, the method returns -1.

        Args:
            path (int): A sequence of vertex identifiers representing the path.

        Returns:
            int: The total weight of the path if it exists, otherwise -1.
            None: If vertex from the given path is not in the graph.
        """
        try:
            self.check_miss_vert(*path)
        except KeyError as e:
            # raise Exception(f"One or more vertices from path {path} does not exist in the graph.") from e
            print(str(e))
            return

        total_path_weight = 0
        for i in range(len(path) - 1):
            vertex1, vertex2 = path[i], path[i+1]
            existing_edge = next((edge for edge in self.graph[vertex1] if edge[0] == vertex2), None)
            if existing_edge:
                total_path_weight += existing_edge[1]
            else:
                return -1
        return total_path_weight

    def check_miss_vert(self, *vertices: int) -> None:
        """Checks if the given vertex or vertices are not in the graph.

        Args:
            vertices (int): Vertex or vertices to check that they are exist in the graph.

        Raises:
            KeyError: If the given vertex or vertices is not in the graph.
        """
        miss_vert = [vertex for vertex in vertices if vertex not in self.graph]
        if miss_vert:
            miss_vert_repr = ', '.join(map(str, miss_vert))
            raise KeyError(f"There {'is' if len(miss_vert) == 1 else 'are'} no "
                           f"{miss_vert_repr} vert{'ex' if len(miss_vert) == 1 else 'ices'} in the graph with "
                           f"{len(self.graph)} vertices.")


if __name__ == "__main__":
    """> 5      # Total num of vertices
       > 2      # Num of edges to add
       > 1 2 15 # 1st
       > 2 3 13 # 2nd
       > 1 2 3  # Path
       28
    """
    graph = WeightedGraph(num_vertices=int(input("Enter num of vertices: ")))
    for i in range(int(input("Enter number of edges: "))):
        v1, v2, w = map(int, input(f"Enter {i+1}{'st' if i == 0 else 'nd' if i == 1 else 'rd' if i == 2 else 'th'} "
                                   f"edge: ").split())
        graph.add_edge(vertex1=v1, vertex2=v2, weight=w)
    print(graph.get_path_weight(*map(int, input("Enter the path to get path weight: ").split())))
