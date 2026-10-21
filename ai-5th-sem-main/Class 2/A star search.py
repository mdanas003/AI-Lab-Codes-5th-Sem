import heapq


def a_star(graph, heuristic, start, goal):

    # Priority queue
    # (f_cost, g_cost, node)
    pq = []

    heapq.heappush(pq, (heuristic[start], 0, start))

    # Actual cost from start to each node
    g_cost = {
        start: 0
    }

    # Parent dictionary for reconstructing path
    parent = {
        start: None
    }

    while pq:

        f, g, current = heapq.heappop(pq)

        # Goal reached
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Path:", " -> ".join(path))
            print("Cost:", g)

            return

        # Explore neighbors
        for neighbor, cost in graph[current]:

            new_g = g + cost

            # If this is a better path
            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                f_cost = new_g + heuristic[neighbor]

                parent[neighbor] = current

                heapq.heappush(
                    pq,
                    (f_cost, new_g, neighbor)
                )

    print("No path found")


graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 1)],
    'C': [('G', 2)],
    'D': [('G', 3)],
    'E': [('G', 4)],
    'G': []
}


heuristic = {
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 3,
    'E': 4,
    'G': 0
}


a_star(graph, heuristic, 'A', 'G')