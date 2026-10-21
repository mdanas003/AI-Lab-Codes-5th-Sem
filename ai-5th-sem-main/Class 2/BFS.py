from collections import deque


def bfs(graph, start, goal):

    # Queue stores (node, path so far)
    queue = deque([(start, [start])])

    visited = {start}

    while queue:

        # FIFO: take the oldest added node
        current, path = queue.popleft()

        print("Visiting:", current)

        if current == goal:
            print("Path:", " -> ".join(path))
            print("Number of edges:", len(path) - 1)
            return

        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("No path found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': ['G'],
    'E': ['G'],
    'G': []
}

bfs(graph, 'A', 'G')
