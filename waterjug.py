
# Water Jug Problem using DFS

def water_jug_dfs(capacity1, capacity2, target):

    visited = set()
    path = []

    def dfs(jug1, jug2):

        if (jug1, jug2) in visited:
            return False

        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        # Check goal
        if jug1 == target or jug2 == target:
            return True

        # Fill Jug 1
        if dfs(capacity1, jug2):
            return True

        # Fill Jug 2
        if dfs(jug1, capacity2):
            return True

        # Empty Jug 1
        if dfs(0, jug2):
            return True

        # Empty Jug 2
        if dfs(jug1, 0):
            return True

        # Pour Jug 1 into Jug 2
        if dfs(max(0, jug1 - (capacity2 - jug2)),
               min(capacity2, jug1 + jug2)):
            return True

        # Pour Jug 2 into Jug 1
        if dfs(min(capacity1, jug1 + jug2),
               max(0, jug2 - (capacity1 - jug1))):
            return True

        # Backtracking
        path.pop()
        return False

    if dfs(0, 0):
        return path

    return []


# Main Program
capacity1 = 3
capacity2 = 5
target = 4

solution = water_jug_dfs(capacity1, capacity2, target)

if solution:
    print("Water Jug Solution:")

    for step, state in enumerate(solution):
        print("Step", step, ":", state)

else:
    print("No solution found.")
