def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """



def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    number_of_nodes = len(graph)

    dist = [float('inf')] * number_of_nodes
    prev = [None] * number_of_nodes
    dist[source] = 0

    # Create a list of nodes to visit
    H = list(range(number_of_nodes))

    while H:
        u = min(H, key=lambda node: dist[node])
        H.remove(u)

        if dist[u] == float('inf') or u == target:
            break

        # for all edges (u, v) in E
        for v, weight in graph[u].items():
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                prev[v] = u

    path = []
    current = target
    if dist[target] == float('inf'):
        return path, dist[target]

    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path, dist[target]


