# Minimax: X is MAX (wants +1), O is MIN (wants -1). Draw = 0.

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


def minimax(board, is_max):

    w = winner(board)
    if w == 'X':
        return 1
    if w == 'O':
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -2
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = 2
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best


def best_move(board, player):
    is_max = player == 'X'
    best_val = -2 if is_max else 2
    move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            val = minimax(board, not is_max)
            board[i] = ' '

            if (is_max and val > best_val) or (not is_max and val < best_val):
                best_val, move = val, i

    return move


# Two perfect players: the game should end in a draw
board = [' '] * 9
turn = 'X'

while winner(board) is None and ' ' in board:
    move = best_move(board, turn)
    board[move] = turn
    print(turn, "plays position", move)
    print_board(board)
    turn = 'O' if turn == 'X' else 'X'

print("Result:", winner(board) or "Draw")
