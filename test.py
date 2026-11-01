from collections import deque


def start(n):
    return (tuple(range(n,0,-1),(),()))

def goal(n):
    return ((),(),tuple(range(n,0,-1)))
            
    
    
def honai(n):
    
       