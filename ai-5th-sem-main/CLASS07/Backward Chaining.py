# Backward chaining (goal-driven): start from the goal and prove
# each premise recursively, down to known facts.

rules = [
    (['A', 'B'], 'C'),   # Rule 1
    (['C'], 'D'),        # Rule 2
    (['D'], 'E')         # Rule 3
]

facts = {'A', 'B'}


def backward_chaining(goal, rules, facts, visited=None, depth=0):

    if visited is None:
        visited = set()

    indent = "  " * depth
    print(indent + "Proving:", goal)

    if goal in facts:
        print(indent + goal, "is a known fact")
        return True

    # Avoid infinite loops on cyclic rules
    if goal in visited:
        return False

    visited = visited | {goal}

    for premises, conclusion in rules:

        if conclusion == goal:

            if all(backward_chaining(p, rules, facts, visited, depth + 1)
                   for p in premises):

                print(indent + goal, "proved using",
                      " and ".join(premises), "->", goal)
                return True

    return False


result = backward_chaining('E', rules, facts)
print("\nGoal E proved:", result)
