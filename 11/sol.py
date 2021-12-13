from itertools import product

with open("input.txt","r") as f:
    txt = f.read()
    grid = [[int(n) for n in l] for l in txt.splitlines()]

def neighbors(grid, r, c):
    for dr, dc in product(range(-1, 2), repeat = 2):    
        if dr == dc == 0:    
            continue    
        if not 0 <= r + dr < len(grid):
            continue    
        if not 0 <= c + dc < len(grid[0]):
            continue    
        yield r + dr, c + dc 

# mutates grid
def step(grid):
    n, m = len(grid), len(grid[0])
    s = []
    for r, c in product(range(n), range(m)):   
        grid[r][c] += 1        
        if grid[r][c] == 10: 
            s.extend(neighbors(grid, r, c))
    while s:
        r, c = s.pop()    
        grid[r][c] += 1   
        if grid[r][c] == 10:
            s.extend(neighbors(grid, r, c))    

    flashes = 0
    for r, c in product(range(n), range(m)):
        if grid[r][c] > 9:
            grid[r][c] = 0    
            flashes += 1
    return flashes

def part1(grid, steps):
    grid = [grid[r][:] for r in range(len(grid))]        
    return sum(step(grid) for _ in range(steps))

def part2(grid):
    total = len(grid) * len(grid[0]) 
    grid = [grid[r][:] for r in range(len(grid))]        
    i = 0
    while step(grid) != total:
        i += 1        
    return i + 1 
