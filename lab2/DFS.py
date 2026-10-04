def dfs(start, goal, max_depth=20):
    stack = [(start, [], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()

        if state == goal:
            return path + [state]

        if depth >= max_depth:
            continue

        if state in visited:
            continue

        visited.add(state)

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)

                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:
                    stack.append(
                        (new_state, path + [state], depth + 1)
                    )

    return None


def print_solution(solution):
    if solution is None:
        print("No solution found.")
        return

    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()


start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

print("DFS Solution:")
solution = dfs(start, goal)