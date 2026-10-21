# Tic-Tac-Toe solved with a basic search strategy (DFS over the game tree).
# The search finds whether X can force a win/draw/loss from a given board,
# then X plays the best move found. O replies with the first free cell.

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None


def print_board(board):
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
    print()


def dfs_value(board, player):
    # Returns +1 if X wins, 0 draw, -1 if O wins (best play by both)
    w = winner(board)
    if w == 'X':
        return 1
    if w == 'O':
        return -1
    if ' ' not in board:
        return 0

    values = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            values.append(dfs_value(board, 'O' if player == 'X' else 'X'))
            board[i] = ' '

    return max(values) if player == 'X' else min(values)


def best_move_for_x(board):
    best, best_val = None, -2
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            val = dfs_value(board, 'O')
            board[i] = ' '
            if val > best_val:
                best, best_val = i, val
    return best


board = [' '] * 9
turn = 'X'

while winner(board) is None and ' ' in board:

    if turn == 'X':
        move = best_move_for_x(board)
    else:
        move = board.index(' ')

    board[move] = turn
    print(turn, "plays position", move)
    print_board(board)

    turn = 'O' if turn == 'X' else 'X'

print("Winner:", winner(board) or "Draw")
