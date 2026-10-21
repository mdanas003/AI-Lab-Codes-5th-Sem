def hill_climbing(graph, heuristic, start, goal):

    current = start

    while True:

        print("Current node:", current)

        # Goal reached
        if current == goal:
            print("Goal found!")
            return

        neighbors = graph[current]

        # If no neighbors
        if not neighbors:
            print("No more moves. Goal not found.")
            return

        # Find the best neighbor
        best_neighbor = current

        for neighbor in neighbors:

            if heuristic[neighbor] < heuristic[best_neighbor]:
                best_neighbor = neighbor

        # No better neighbor exists
        if best_neighbor == current:
            print("Reached a local optimum.")
            print("Goal not found.")
            return

        # Move to better neighbor
        current = best_neighbor


# --------------------------------
# Graph
# --------------------------------

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
# Smaller value = closer to goal

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 4,
    'F': 3,
    'G': 0
}


# Start and goal
start = 'A'
goal = 'G'

hill_climbing(graph, heuristic, start, goal)