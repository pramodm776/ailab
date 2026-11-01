import heapq

start = (1 ,2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def h(s):
    return sum(abs(i//3 - goal.index(x)//3) + abs(i%3 - goal.index(x)%3) for i, x in enumerate(s) if x!= 0)

def astar():
    
    pd = [(h(start),0,start,[start])]
    
    visited = {start: 0}
    
    while pd:
        f,g,s,path = heapq.heappop(pd)
        
        if s == goal:
            return path
        
        z = s.index(0)
        
        for d in [-3, 3, -1, 1]:
            n=  z+d
            
            if 0 <=n <9 and not(( d==-1 and z%3==0) or (d =-1 and z%3 == 2)):
                t = list(s)
                t[z],t[n] = t[n],t[z]
                
                t = tuple(t)
                ng = g+1
