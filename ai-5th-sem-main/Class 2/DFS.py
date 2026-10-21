def dfs(graph, start, goal):

    # Stack stores (node, path so far)
    stack = [(start, [start])]

    visited = set()

    while stack:

        # LIFO: take the most recently added node
        current, path = stack.pop()

        if current in visited:
            continue

        print("Visiting:", current)

        visited.add(current)

        if current == goal:
            print("Path:", " -> ".join(path))
            return

        # Reverse so the first neighbor is explored first
        for neighbor in reversed(graph[current]):

            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    print("No path found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': ['G'],
    'E': ['G'],
    'G': []
}

dfs(graph, 'A', 'G')
