N = 8

board = [['.' for _ in range(N)] for _ in range(N)]

cols = set()
dig1 = set()
dig2 = set()

def solve(row):
    if row == N:
        return True
    
    for col in range(N):
        if col not in cols and row - col not in dig1 and row + col not in dig2:
            
            board[row][col] = 'Q'
            cols.add(col)
            dig1.add(row-col)
            dig2.add(row+col)
            
            
            if solve(row +1):
                return True
            
            
            # backtracking
            
            board[row][col] = '.'
            cols.remove(col)
            dig1.remove(row-col)
            dig2.remove(row+col)
    
    
    
    return False



if solve(0):
    print("Solution")
    
    for row in board:
        print(' '.join(row))
        
    
    
else:
    
    print("No solution")
    