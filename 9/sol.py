from heapq import heappush, heappushpop

def parse_line(l):
    return [int(c) for c in l]    


with open("input.txt", "r") as f:
    txt = f.read() 
    grid = [parse_line(l) for l in txt.splitlines()]

def neighbors(grid, r, c):
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            yield r + dr, c + dc

def floodfill(grid, r, c):
    if grid[r][c] is None or grid[r][c] == 9: 
        return 0    
    s, grid[r][c] = 1, None
    for nr, nc in neighbors(grid, r, c):
        s += floodfill(grid, nr, nc)    
    return s
                

def part1(grid):
    s = 0
    for r in range(len(grid)):    
        for c in range(len(grid[0])):    
            if all(grid[r][c] < grid[nr][nc] for nr, nc in neighbors(grid, r, c)):
                s += grid[r][c] + 1
    return s

def part2(grid):
    h = []
    for r in range(len(grid)):        
        for c in range(len(grid[0])):    
            res = floodfill(grid, r, c)
            if len(h) < 3:
                heappush(h, res)        
            elif res > h[0]:
                heappushpop(h, res)    
    p = 1
    for n in h:
        p *= n
    return p

print(part1(grid))
print(part2(grid))
