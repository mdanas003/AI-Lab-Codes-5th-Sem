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


def dfs(start, goal):

    stack = [(start, [start])]
    visited = {start}

    while stack:

        state, path = stack.pop()

        if state == goal:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                visited.add(neighbor)

                stack.append(
                    (neighbor, path + [neighbor])
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

path = dfs(start, goal)

if path:

    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:
        print_puzzle(state)

else:
    print("No solution found.")