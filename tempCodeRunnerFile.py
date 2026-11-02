dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(p):
    return sum(dist[p[i]][p[i+1]] for i in range(3)) + dist[p[3]][p[0]]

beam = [[0, 1, 2, 3], [0, 2, 3, 1]]

for _ in range(5):
    new = []

    for p in beam:
        for i in range(1, 4):
            q = p[:]
            j = i % 3 + 1
            q[i], q[j] = q[j], q[i]
            new.append(q)

    beam = sorted(new, key=cost)[:2]

best = min(beam, key=cost)

print("Best Path:", best + [best[0]])
print("Minimum Distance:", cost(best))

