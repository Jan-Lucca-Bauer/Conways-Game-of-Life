from collections import Counter
from data.rules import RuleMode

def next_generation(alive_cells: set[tuple[int, int]], rule: RuleMode) -> set[tuple[int, int]]:
    # Creates a counter for counting how many neighbors each alive cell has.
    neighbor_counts = Counter()

    for x, y in alive_cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                neighbor_counts[(x + dx, y + dy)] += 1

    next_cells = set()

    for cell, count in neighbor_counts.items():
        if cell in alive_cells:
            if count in rule.value.survival:
                next_cells.add(cell)

        elif count in rule.value.birth:
            next_cells.add(cell)

    return next_cells