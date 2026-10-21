import heapq


def manhattan(state, goal):

    distance = 0

    for i in range(9):

        if state[i] == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_index = goal.index(state[i])

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def best_first_search(start, goal):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (manhattan(start, goal), start, [start])
    )

    visited = set()

    while priority_queue:

        h, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                heapq.heappush(
                    priority_queue,
                    (
                        manhattan(neighbor, goal),
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

path = best_first_search(start, goal)

if path:

    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:
        print_puzzle(state)

else:
    print("No solution found.")