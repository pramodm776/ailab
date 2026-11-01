import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(abs(i//3 - goal.index(x)//3) +
               abs(i%3 - goal.index(x)%3)
               for i, x in enumerate(s) if x != 0)

def astar():
    q = [(h(start), start, [])]
    visited = set()

    while q:
        f, s, path = heapq.heappop(q)

        if s == goal:
            return path + [s]

        if s in visited:
            continue

        visited.add(s)
        z = s.index(0)

        for d in [-3, 3, -1, 1]:
            n = z + d

            if 0 <= n < 9 and not (
                (d == -1 and z % 3 == 0) or
                (d == 1 and z % 3 == 2)
            ):
                t = list(s)
                t[z], t[n] = t[n], t[z]
                t = tuple(t)

                if t not in visited:
                    heapq.heappush(q, (len(path)+1+h(t), t, path+[s]))

    return None

result = astar()

if result:
    for step, s in enumerate(result):
        print("Step", step)
        for i in range(0, 9, 3):
            print(s[i:i+3])
else:
    print("No solution")