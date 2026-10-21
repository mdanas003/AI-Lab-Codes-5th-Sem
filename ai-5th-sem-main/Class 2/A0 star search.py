# AO* Algorithm in Python

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.solved = False
        self.children = []


def ao_star(node):
    # If node is already solved
    if node.solved:
        return node.heuristic

    # If node has no children, it is a goal/terminal node
    if not node.children:
        node.solved = True
        return node.heuristic

    # Find the best option among OR choices
    best_cost = float('inf')
    best_group = None

    for group in node.children:

        # group represents an AND set
        # All nodes in the group must be solved
        cost = 0

        for child in group:
            cost += child.heuristic

        if cost < best_cost:
            best_cost = cost
            best_group = group

    # Solve all nodes in the best AND group
    total_cost = 0

    for child in best_group:
        total_cost += ao_star(child)

    node.heuristic = total_cost
    node.solved = True

    print("Solved:", node.name)

    return node.heuristic


# ------------------------------------------------
# Creating the AND-OR graph
# ------------------------------------------------

A = Node("A", 10)
B = Node("B", 4)
C = Node("C", 6)
D = Node("D", 2)
E = Node("E", 3)
F = Node("F", 4)

# A is an OR node:
#
#        A
#       / \
#      B   C
#
# We can choose B OR C.
#
# B is an AND node:
#
#        B
#       / \
#      D   E
#
# So B requires both D AND E.

A.children = [
    [B],          # Option 1: B
    [C]           # Option 2: C
]

B.children = [
    [D, E]        # B requires D AND E
]


# ------------------------------------------------
# Run AO*
# ------------------------------------------------

cost = ao_star(A)

print("\nMinimum cost:", cost)