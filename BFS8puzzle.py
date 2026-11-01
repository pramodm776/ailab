from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def bfs():
    q = deque([(start, [start])])
    visited = {start}
    
    while q:
        state, path = q.popleft()
        
        if state == goal:
            return path
        
        z = state.index(0)
        
        for d in [-3,3,-1,1]:
            n = z +d
            
            if 0 <=n<9 and not ((d==-1 and z%3==0) or (d==1 and z%3==2)):
                new = list(state)
                new[z], new[n] = new[n], new[z]
                new = tuple(new)
                
                
                if new not in visited:
                    visited.add(new)
                    q.append((new, path+[new]))
                    
                    
    return None


path = bfs()


if path:
    for step, state in enumerate(path):
        print("step:", step)
        
        for i in range(0,9,3):
            print(state[i:i+3])
            
            
else:
    print("No solution")