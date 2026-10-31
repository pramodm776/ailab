
from collections import deque

# Initial state
def get_initial_state(n):
    return (tuple(range(n, 0, -1)), (), ())

# Goal state
def get_goal_state(n):
    return ((), (), tuple(range(n, 0, -1)))

# Generate all possible legal moves
def get_successors(state):
    successors = []

    for source in range(3):
        for target in range(3):

            if source == target:
                continue

            if not state[source]:
                continue

            disk = state[source][-1]

            if state[target] and state[target][-1] < disk:
                continue

            new_state = [list(peg) for peg in state]

            new_state[source].pop()
            new_state[target].append(disk)

            next_state = tuple(tuple(peg) for peg in new_state)

            successors.append((next_state, (source, target)))

    return successors

# Solve using BFS
def solve_hanoi(n):
    start = get_initial_state(n)
    goal = get_goal_state(n)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for next_state, action in get_successors(current):

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return None

# Display solution
def print_solution(path):
    if path is None:
        print("No solution found")
        return

    peg = {0: 'A', 1: 'B', 2: 'C'}

    print("Tower of Hanoi Solution")
    print("Minimum moves:", len(path))

    for i, (src, dst) in enumerate(path, 1):
        print("Step", i, ": Move disk from",
              peg[src], "to", peg[dst])

# Main program
n = 3

solution = solve_hanoi(n)
print_solution(solution)
