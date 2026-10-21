import heapq


def best_first_search(graph, heuristic, start, goal):
    # Priority queue
    # Stores: (heuristic value, node)
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start))

    # To keep track of visited nodes
    visited = set()

    while priority_queue:

        # Get node with smallest heuristic value
        h, current = heapq.heappop(priority_queue)

        # Skip if already visited
        if current in visited:
            continue

        print("Visiting:", current)

        visited.add(current)

        # Check if goal is reached
        if current == goal:
            print("Goal found!")
            return

        # Add all unvisited neighbours
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal not found!")


# -------------------------------
# Main Program
# -------------------------------

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 4,
    'F': 3,
    'G': 0
}


start = 'A'
goal = 'G'

best_first_search(graph, heuristic, start, goal)