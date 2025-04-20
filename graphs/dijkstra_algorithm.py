import heapq


def dijkstra(adj_matrix, start, end):
    """Finds the shortest path between two nodes using Dijkstra's algorithm.

    This function computes the shortest path from a given start node to a given end node
    in a weighted graph represented by an adjacency matrix. It uses a priority queue
    to always expand the nearest unvisited node.

    Args:
        adj_matrix (list[list[int]]): Adjacency matrix representing the graph.
            A 0 indicates no direct connection (except diagonals).
        start (int): Index of the starting node.
        end (int): Index of the target node.

    Returns:
        list[str]: A list of node indices (as strings) representing the shortest path from start to end.
    """
    n = len(adj_matrix)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > dist[u]:
            continue

        for v in range(n):
            weight = adj_matrix[u][v]
            if weight != 0:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))

    path = []
    if dist[end] == float('inf'):
        return path

    while end is not None:
        path.insert(0, str(end))
        end = prev[end]

    return path


am = [
    [0, 4, 4, 0, 0, 0],
    [4, 0, 2, 0, 0, 0],
    [4, 2, 0, 3, 1, 6],
    [0, 0, 3, 0, 0, 2],
    [0, 0, 1, 0, 0, 3],
    [0, 0, 6, 2, 3, 0]
]

a, b = (int(x) for x in input().split())

short_path = dijkstra(am, a, b)

print(f"A shortest path from {a} to {b} is: {' '.join(short_path)}.")
