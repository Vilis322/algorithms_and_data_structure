def floyd(adj_matrix):
    """Computes shortest paths between all pairs of nodes using Floyd-Warshall algorithm.

    The function returns two matrices:
    - dist: matrix of shortest distances
    - pred: matrix of predecessors to reconstruct shortest paths

    Args:
        adj_matrix (list[list[int]]): Adjacency matrix representing the graph.
            A 0 (except on diagonal) indicates no direct edge.

    Returns:
        tuple: A tuple (dist, pred), where:
            - dist is a 2D list of shortest path distances,
            - pred is a 2D list of predecessors for path reconstruction.
    """
    n = len(adj_matrix)

    dist = [[float('inf') if i != j and adj_matrix[i][j] == 0 else adj_matrix[i][j]
             for j in range(n)] for i in range(n)]
    pred = [[None if i == j or adj_matrix[i][j] == 0 else i
             for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


def reconstruct_path(pred, a, b):
    """Reconstructs shortest path from node a to b using predecessor matrix.

    Args:
        pred (list[list[int]]): Predecessor matrix from Floyd-Warshall.
        a (int): Start node.
        b (int): End node.

    Returns:
        list: The list of nodes representing the shortest path from a to b.
    """
    path = []
    if pred[a][b] is None:
        return path
    while b != a:
        path.insert(0, b)
        b = pred[a][b]
    path.insert(0, a)
    return list(map(str, path))


am = [
    [0, 4, 4, 0, 0, 0],
    [4, 0, 2, 0, 0, 0],
    [4, 2, 0, 3, 1, 6],
    [0, 0, 3, 0, 0, 2],
    [0, 0, 1, 0, 0, 3],
    [0, 0, 6, 2, 3, 0]
]

a, b = (int(x) for x in input().split())

dist, pred = floyd(am)

short_path = reconstruct_path(pred, a, b)

print(f"A shortest path from {a} to {b} is: {' '.join(short_path)}.")
