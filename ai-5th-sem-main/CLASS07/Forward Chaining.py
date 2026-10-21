# Forward chaining (data-driven): start from facts, fire rules until
# the goal is derived or nothing new can be added.

# Each rule: (list of premises, conclusion)
rules = [
    (['A', 'B'], 'C'),   # Rule 1
    (['C'], 'D'),        # Rule 2
    (['D'], 'E')         # Rule 3
]

facts = {'A', 'B'}


def forward_chaining(rules, facts, goal):

    facts = set(facts)
    changed = True

    while changed:

        changed = False

        for premises, conclusion in rules:

            if conclusion not in facts and all(p in facts for p in premises):

                facts.add(conclusion)
                changed = True

                print("Rule fired:", " and ".join(premises),
                      "->", conclusion)

                if conclusion == goal:
                    print("Goal", goal, "derived!")
                    return True

    return goal in facts


result = forward_chaining(rules, facts, 'E')
print("Goal reached:", result)
