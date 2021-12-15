from math import inf
from heapq import heappush, heappop, heappushpop
from collections import defaultdict  

with open("input.txt", "r") as f:
    txt = f.read()    
    grid = [[int(c) for c in row] for row in txt.splitlines()]


def neighbors(grid, r, c):
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:    
        if not 0 <= r + dr < len(grid):    
            continue    
        if not 0 <= c + dc < len(grid[0]):
            continue     
        yield r + dr, c + dc

def solve(grid):
    dists = defaultdict(lambda: inf) 
    h = [(0, 0, 0)] 
    while h:
        w, r, c = heappop(h)    
        for nr, nc in neighbors(grid, r, c):  
            if (nw := w + grid[nr][nc]) < dists[(nr, nc)]: 
                dists[(nr, nc)] = nw
                heappush(h, (nw, nr, nc)) 
    return dists[(len(grid) - 1, len(grid[0]) - 1)]

def increase(n):
    if n == 9:    
        return 1    
    return n + 1

def repeat(grid, k):
    grid = [grid[r][:] for r in range(len(grid))]
    n, m = len(grid), len(grid[0])

    for _ in range(k):  
        for r in range(n):
            grid[r].extend(map(increase, grid[r][-n:]))

    for _ in range(k):
        for r in range(n):    
            grid.append([increase(d) for d in grid[- n]])
            
    return grid

print(solve(grid))
print(solve(repeat(grid, 4)))
