from abc import ABC, abstractmethod
from collections import defaultdict


class GraphInterface(ABC):
    @abstractmethod
    def __init__(self, num_vertices: int):
        super().__init__()
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    @abstractmethod
    def add_edge(self, v1: int, v2: int) -> None:
        pass

    @abstractmethod
    def is_adjacent(self, v1: int, v2: int) -> bool:
        pass

    @abstractmethod
    def return_adjacent(self, v: int) -> list[int]:
        pass


class WeightedGraphInterface(GraphInterface):
    @abstractmethod
    def add_edge(self, v1: int, v2: int, w: int) -> None:
        pass


class Graph(GraphInterface):
    """Represents an undirected graph."""
    def __init__(self):
        """Initializes an empty graph."""
        super().__init__(num_vertices=0)

    def add_edge(self, v1: int, v2: int) -> None:
        """Adds an undirected edge between vertices v1 and v2.

        If v1 or v2 vertices are not exist in the graph, they are added,
        and the count of the number of vertices (num_vertices) is incremented.

        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
        """
        if v1 not in self.graph:
            self.num_vertices += 1
        if v2 not in self.graph:
            self.num_vertices += 1

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
        return

    def is_adjacent(self, v1: int, v2: int) -> bool:
        """Checks if vertices v1 and v2 are adjacent.

        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.

        Returns:
            bool: True if v2 vertex is in v1 vertex's adjacency list, otherwise False.
        """
        return v2 in self.graph.get(v1)

    def return_adjacent(self, v: int) -> list[int]:
        """Returns a list of adjacent vertices for the given vertex v.

        Args:
            v (int): The vertex for which to get the list of adjacent vertices.

        Returns:
            list[int]: A list of adjacent vertices. If the vertex is not in the graph, an empty list is returned.
        """
        return self.graph.get(v, [])


class DirectedGraph(GraphInterface):
    """Represents a directed graph."""
    def __init__(self):
        """Initializes an empty directed graph."""
        super().__init__(num_vertices=0)

    def add_edge(self, v1: int, v2: int) -> None:
        """Adds a directed edge from vertex v1 to vertex v2.

        If v1 or v2 vertices are not exist in the graph, they are added,
        and the count of the number of vertices (num_vertices) is incremented.

        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
        """
        if v1 not in self.graph:
            self.num_vertices += 1
        if v2 not in self.graph:
            self.graph.setdefault(v2, [])
            self.num_vertices += 1

        self.graph[v1].append(v2)
        return

    def is_adjacent(self, v1: int, v2: int) -> bool:
        """Checks if vertices v1 and v2 are adjacent.

        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.

        Returns:
            bool: True if v2 vertex is in v1 vertex's adjacency list, otherwise False.
        """
        return v2 in self.graph.get(v1)

    def return_adjacent(self, v: int) -> list[int]:
        """Returns a list of adjacent vertices for the given vertex v.

        Args:
            v (int): The vertex for which to get the list of adjacent vertices.

        Returns:
            list[int]: A list of adjacent vertices. If the vertex is not in the graph, an empty list is returned.
        """
        return self.graph.get(v, [])


class WeightedGraph(WeightedGraphInterface):
    """Represents an undirected weighted graph."""
    def __init__(self):
        """Initializes an empty weighted graph."""
        super().__init__(num_vertices=0)

    def add_edge(self, v1: int, v2: int, w: int) -> None:
        """Adds an undirected edge between vertices v1 and v2 and weight for this edge.

        If v1 or v2 vertices are not exist in the graph, they are added,
        and the count of the number of vertices (num_vertices) is incremented.

        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.
            w (int): The weight of the edge.
        """
        if v1 not in self.graph:
            self.num_vertices += 1
        if v2 not in self.graph:
            self.num_vertices += 1

        self.graph[v1].append((v2, w))
        self.graph[v2].append((v1, w))
        return

    def is_adjacent(self, v1: int, v2: int) -> bool:
        """Checks if vertices v1 and v2 are adjacent.

        Args:
            v1 (int): The first vertex.
            v2 (int): The second vertex.

        Returns:
            bool: True if v2 vertex is in v1 vertex's adjacency list, otherwise False.
        """
        return any(adj_vertex == v2 for adj_vertex, _ in self.graph.get(v1, []))

    def return_adjacent(self, v: int) -> list[tuple[int, int]]:
        """Returns a list of adjacent vertices for the given vertex v.

        Args:
            v (int): The vertex for which to get the list of adjacent vertices.

        Returns:
            list[tuple[int, int]]: A list of adjacent vertices and their weight.
            If the vertex is not in the graph, an empty list is returned.
        """
        return self.graph.get(v, [])


if __name__ == "__main__":
    graph = Graph()

    # Add edges
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # Check adjacency
    print("Is 1 adjacent to 2?", graph.is_adjacent(1, 2))  # True
    print("Is 1 adjacent to 3?", graph.is_adjacent(1, 3))  # False

    # Get adjacent vertices
    print("Adjacent vertices to 2:", graph.return_adjacent(2))  # [1, 3]
    print("Adjacent vertices to 3:", graph.return_adjacent(3))  # [2, 4]
    print("Adjacent vertices to 4:", graph.return_adjacent(4))  # [3]

    # Check non-existing vertex
    print("Adjacent vertices to 5:", graph.return_adjacent(5))  # []

    directed_graph = DirectedGraph()

    # Add directed edges
    directed_graph.add_edge(1, 2)
    directed_graph.add_edge(2, 3)
    directed_graph.add_edge(3, 4)

    # Check adjacency
    print("Is 1 adjacent to 2?", directed_graph.is_adjacent(1, 2))  # True
    print("Is 2 adjacent to 1?", directed_graph.is_adjacent(2, 1))  # False
    print("Is 2 adjacent to 3?", directed_graph.is_adjacent(2, 3))  # True
    print("Is 3 adjacent to 2?", directed_graph.is_adjacent(3, 2))  # False

    # Get adjacent vertices
    print("Adjacent vertices to 2:", directed_graph.return_adjacent(2))  # [3]
    print("Adjacent vertices to 3:", directed_graph.return_adjacent(3))  # [4]
    print("Adjacent vertices to 4:", directed_graph.return_adjacent(4))  # []

    # Check non-existing vertex
    print("Adjacent vertices to 5:", directed_graph.return_adjacent(5))  # []

    weighted_graph = WeightedGraph()

    # Add undirected edges with weights
    weighted_graph.add_edge(1, 2, 10)
    weighted_graph.add_edge(2, 3, 20)
    weighted_graph.add_edge(3, 4, 30)

    # Check adjacency
    print("Is 1 adjacent to 2?", weighted_graph.is_adjacent(1, 2))  # True
    print("Is 2 adjacent to 1?", weighted_graph.is_adjacent(2, 1))  # True
    print("Is 2 adjacent to 3?", weighted_graph.is_adjacent(2, 3))  # True
    print("Is 3 adjacent to 2?", weighted_graph.is_adjacent(3, 2))  # True
    print("Is 3 adjacent to 1?", weighted_graph.is_adjacent(3, 1))  # False

    # Get adjacent vertices and their weights
    print("Adjacent vertices to 2:", weighted_graph.return_adjacent(2))  # [(1, 10), (3, 20)]
    print("Adjacent vertices to 3:", weighted_graph.return_adjacent(3))  # [(2, 20), (4, 30)]
    print("Adjacent vertices to 4:", weighted_graph.return_adjacent(4))  # [(3, 30)]
    print("Adjacent vertices to 5:", weighted_graph.return_adjacent(5))  # []
