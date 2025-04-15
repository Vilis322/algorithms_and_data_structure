def kruskal(adj_list) -> None:
    """Computes the total weight of the Minimum Spanning Tree (MST) using Kruskal's algorithm.

    This function implements Kruskal's algorithm for a given undirected, weighted graph
    represented as an adjacency list. It works by:
    1. Extracting all edges from the graph.
    2. Sorting them in ascending order of weight.
    3. Iteratively selecting the smallest edge that connects two disjoint components
        (using a simple Union-Find mechanism).
    4. Accumulating the total weight of the MST without forming cycles.

    Args:
        adj_list (dict): Adjacency list where each node maps to its neighbors and edge weights.

    Returns:
        None: The function prints the step-by-step process and the total weight of the MST.
    """
    total = 0
    edges = []

    #  Collect all edges, avoiding duplicates
    for u in adj_list:
        for v in adj_list[u]:
            if (v, u, adj_list[u][v]) not in edges:
                edges.append((u, v, adj_list[u][v]))

    edges.sort(key=lambda x: x[2])

    print("Sorted edges:")
    for e in edges:
        print(f"  {e}")
    print()

    parent = {node: node for node in adj_list}
    print(f"Initial parent mapping: {parent}")
    print()

    for u, v, weight in edges:
        root_u = u
        while parent[root_u] != root_u:
            root_u = parent[root_u]

        root_v = v
        while parent[root_v] != root_v:
            root_v = parent[root_v]

        print(f"Processing edge ({u}, {v}) with weight {weight}")
        print(f"  Root of {u}: {root_u}, Root of {v}: {root_v}")

        if root_u != root_v:
            parent[root_u] = root_v  # Union
            total += weight
            print(f"   Edge added. Updated parent: {root_u} → {root_v}")
            print(f"   Current MST total weight: {total}")
        else:
            print(f"   Edge skipped to avoid cycle.")

        print(f"  Current parent mapping: {parent}\n")

    print(f"Total spanning tree weight is {total}")


graph = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 1, 'F': 6},
    'D': {'C': 3, 'F': 2},
    'E': {'C': 1, 'F': 3},
    'F': {'C': 6, 'D': 2, 'E': 3},
}

kruskal(graph)
