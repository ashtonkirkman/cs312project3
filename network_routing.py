from priority_queues import LinearPQ, HeapPQ


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
    number_of_nodes = len(graph)

    dist = [float('inf')] * number_of_nodes
    prev = [None] * number_of_nodes
    dist[source] = 0

    # Create a list of nodes to visit
    pq = HeapPQ()
    for node in range(number_of_nodes):
        pq.insert(node, dist[node])

    while not pq.is_empty():
        u = pq.delete_min()

        if dist[u] == float('inf') or u == target:
            break

        # for all edges (u, v) in E
        for v, weight in graph[u].items():
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                prev[v] = u
                pq.decrease_key(v, dist[v])

    path = []
    current = target
    if dist[target] == float('inf'):
        return path, dist[target]

    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path, dist[target]


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
    pq = LinearPQ()
    for node in range(number_of_nodes):
        pq.insert(node, dist[node])

    while not pq.is_empty():
        u = pq.delete_min()

        if dist[u] == float('inf') or u == target:
            break

        # for all edges (u, v) in E
        for v, weight in graph[u].items():
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                prev[v] = u
                pq.decrease_key(v, dist[v])

    path = []
    current = target
    if dist[target] == float('inf'):
        return path, dist[target]

    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path, dist[target]


if __name__ == '__main__':
    queue = LinearPQ()
    queue.insert(1, 2.125)
    queue.insert(2, 1.125)
    queue.insert(3, 4.125)
    queue.insert(4, 3.125)

    minimum = queue.delete_min()
