class Board:
    def __init__(self, grid):
        n, m = len(grid), len(grid[0])
        self.elems = {grid[r][c]:(r, c) for r in range(n) for c in range(m)}
        self.rows = [m for _ in range(n)] 
        self.cols = [n for _ in range(m)]
            
    def mark(self, n):
        if n not in self.elems:
            return False
        
        r, c = self.elems[n]    
        del self.elems[n]
        self.rows[r] -= 1
        self.cols[c] -= 1
        return self.rows[r] == 0 or self.cols[c] == 0

    def remaining(self):
        return self.elems.keys()    

def parse_grid(txt):
    grid = []
    for row in txt.split("\n"):
        if not row:    
            continue
        grid.append([int(e) if e != "_" else e for e in row.split(" ") if e])
    return grid


with open("input.txt") as f:
    txt = f.read()
    nums_line, _, lines = txt.split("\n", 2)
    nums = [int(s) for s in nums_line.split(",")]
    grids = [parse_grid(bt) for bt in lines.split("\n\n")]
    
def mark_number(boards, n): 
    remove = [] 
    for board in boards:
        if board.mark(n):
            remove.append(board)
    return remove


def part1(nums, grids):
    boards = [Board(g) for g in grids]
    for n in nums:        
        if (rem := mark_number(boards, n)):
            return sum(rem[0].remaining()) * n

def part2(nums, grids):
    boards = [Board(g) for g in grids]
    nums = nums.__iter__()
    while len(boards):
        n = next(nums)
        if (rem := mark_number(boards, n)):
            for b in rem:    
                boards.remove(b)
    return sum(b.remaining()) * n

print(part1(nums, grids))
print(part2(nums, grids))
