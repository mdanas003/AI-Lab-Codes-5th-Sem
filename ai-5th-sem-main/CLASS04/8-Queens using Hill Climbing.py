import random


N = 8


def conflicts(board):

    count = 0

    for i in range(N):

        for j in range(i + 1, N):

            # Same column
            if board[i] == board[j]:
                count += 1

            # Same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count


def get_neighbors(board):

    neighbors = []

    for row in range(N):

        for col in range(N):

            if col != board[row]:

                new_board = board.copy()

                new_board[row] = col

                neighbors.append(new_board)

    return neighbors


def hill_climbing():

    board = [random.randint(0, N - 1) for _ in range(N)]

    while True:

        current_score = conflicts(board)

        if current_score == 0:
            return board

        neighbors = get_neighbors(board)

        best = min(
            neighbors,
            key=conflicts
        )

        best_score = conflicts(best)

        if best_score >= current_score:
            return None

        board = best


solution = None

while solution is None:

    solution = hill_climbing()


print("Solution:", solution)
print("Conflicts:", conflicts(solution))

for row in range(N):

    for col in range(N):

        if solution[row] == col:
            print("Q", end=" ")
        else:
            print(".", end=" ")

    print()