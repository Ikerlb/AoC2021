from collections import deque
from math import inf

with open("test.txt","r") as f:
    grid = tuple(f.read().splitlines())

def final_position(grid):
    a = grid[2][3] == "A" and grid[3][3] == "A"    
    b = grid[2][5] == "B" and grid[3][5] == "B"    
    c = grid[2][7] == "C" and grid[3][7] == "C"
    d = grid[2][9] == "D" and grid[3][9] == "D"
    return a and b and c and d

def outside_rooms_cleared(grid):
    return grid[1][3] == grid[1][5] == grid[1][7] == grid[1][9]
    
def neighbors(grid, r, c):
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if  not (0<=r+dr<len(grid) and 0<=c+dc<len(grid[0])):
            continue    
        if grid[r + dr][c + dc] != ".":
            continue    
        yield r + dr, c + dc    

def dist_to(grid, sr, sc, tr, tc):
    q = deque([sr, sc])
    visited = {(sr, sc)}
    dist = 0
    while q:      
        for _ in range(len(q)):    
            r, c = q.popleft()                
            if sr == sc:
                return dist
            for nr, nc in neighbors(grid, r, c):
                if (nr, nc) not in visited:     
                    s.add((nr, nc))
                    q.append((nr, nc))    
        dist += 1
    return None

def possible_moves(grid):                            
    m = []
    for i in range(4): 
        r, c = 2, 2 * i + 3
        e = grid[r][c]
        b = grid[r + 1][c]
        if e == ".":
            continue    
        # if column is set (e == chr(i + ord("A")))
        # then do nothing but theres the case 
        # that col upper is ok, but lower isn't
        if e != chr(i + ord("A")) or b != chr(i + ord("A")): 
                        
                    
                                                            
d = {"A":1,"B":10,"C":100,"D":1000}
    
#@lru_cache(None)
def idfk(grid):
    if final_position(grid):
        return 0    
