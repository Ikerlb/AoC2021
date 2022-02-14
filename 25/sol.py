from math import inf

def parse_line(l):
    return list(l)    

with open("input.txt", "r") as f:
    grid = [parse_line(l) for l in f.read().splitlines()]    
    

def step_horizontal(grid):
    moved = 0
    ngrid = [grid[r][:] for r in range(len(grid))]
    n, m = len(grid), len(grid[0])
    for r in range(n):    
        for c in range(m):    
            if grid[r][c] == ">" and grid[r][(c + 1) % m] == ".":
                ngrid[r][c] = "."    
                ngrid[r][(c + 1) % m] = ">"
                moved += 1
    return moved, ngrid

def step_vertical(grid):
    moved = 0
    ngrid = [grid[r][:] for r in range(len(grid))]
    n, m = len(grid), len(grid[0])    
    for r in range(n):
        for c in range(m):    
            if grid[r][c] == "v" and grid[(r + 1) % n][c] == ".":
                ngrid[r][c] = "."    
                ngrid[(r + 1) % n][c] = "v"
                moved += 1
    return moved, ngrid

def step(grid):
    m1, grid = step_horizontal(grid) 
    m2, grid = step_vertical(grid) 
    return m1 + m2, grid

def part1(grid):
    i = 0
    while (r := step(grid))[0] != 0:      
        m, grid = r
        i += 1
    return i + 1
