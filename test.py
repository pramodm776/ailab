from collections import deque


def startx(n):
    return (tuple(range(n,0,-1)),(),())

def goalx(n):
    return ((),(),tuple(range(n,0,-1)))
            
    
    
def succ(state):
    
    succ = []
    
    for source in range(3):
        for target in range(3):
            
            if source == target:
                continue
            
            if not state[source]:
                continue
            
            disk = state[source][-1]
            
            if state[target] and state[target][-1]<disk:
                continue
            
            newstate = [list(peg) for peg in state]
            
            newstate[source].pop()
            newstate[target].append(disk)
            
            newstate = tuple(tuple(peg) for peg in newstate)
            
            succ.append((newstate,(source, target)))
            
            
    return succ



def honoi(n):
    
    start = startx(n)
    goal = goalx(n)
    
    q = deque([(start, [])])
    
    visit = {start}
                
                
    while q:
        curr, path = q.popleft()
        
        if curr == goal:
            return path
        
        
        for newstate, action in succ(curr):
            
            if newstate not in visit:
                
                visit.add(newstate)
                q.append((newstate, path + [action]))
                
                
    return None

def printx(path):
    if path is None:
        print("no")
        return
    
    peg = {0:'A', 1:'B', 2:'C'}
    for i , (src, des) in enumerate(path,1):
        print("step",i," move form", peg[src],"to", peg[des])
        
        
n = 3  
sol = honoi(n)
printx(sol)



        


    
                
                
            
    
    
    