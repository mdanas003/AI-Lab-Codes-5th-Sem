# Minimax on a small game tree, with and without alpha-beta pruning.
# Leaves are numbers; internal nodes are lists.

tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

count = 0


def minimax(node, is_max):
    global count

    if not isinstance(node, list):
        count += 1
        return node

    values = [minimax(child, not is_max) for child in node]
    return max(values) if is_max else min(values)


def alpha_beta(node, is_max, alpha, beta):
    global count

    if not isinstance(node, list):
        count += 1
        return node

    if is_max:
        value = float('-inf')
        for child in node:
            value = max(value, alpha_beta(child, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node:
            value = min(value, alpha_beta(child, True, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


print("Minimax value:", minimax(tree, True), "| leaves checked:", count)

count = 0
print("Alpha-Beta value:", alpha_beta(tree, True, float('-inf'), float('inf')),
      "| leaves checked:", count)
