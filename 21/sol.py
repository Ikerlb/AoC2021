from functools import lru_cache

class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"[{self.x}, {self.y}]"    

    def __iter__(self):
        yield self.x    
        yield self.y    

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    p1 = int(lines[0].split(": ")[-1]) - 1
    p2 = int(lines[1].split(": ")[-1]) - 1

# mutates scores and pos
def step(scores, pos, roll, turn):
    s = 3 * roll + 3
    pos[turn] = (pos[turn] + s) % 10
    scores[turn] += pos[turn] + 1

def part1(p1, p2):
    scores = [0, 0]
    pos = [p1, p2]
    turn, roll = 0, 1
    
    while not any(s >= 1000 for s in scores):
        step(scores, pos, roll, turn)        
        turn = 1 - turn
        roll += 3

    return min(scores) * (roll - 1)

@lru_cache(None)
def dp(s1, s2, p1, p2, turn):
    if s1 >= 21:
        return Vector(1, 0)
    if s2 >= 21:
        return Vector(0, 1)    
    s = Vector(0, 0)
    if turn == 0:
        for k,v in [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]:
            np = (p1 + k) % 10 
            ns = s1 + np + 1
            s = s.add(dp(ns, s2, np, p2, 1).scale(v))
    else:
        for k,v in [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]:
            np = (p2 + k) % 10 
            ns = s2 + np + 1
            s = s.add(dp(s1, ns, p1, np, 0).scale(v))
    return s

def part2(p1, p2):
    return max(dp(0, 0, p1, p2, 0))

print(part1(p1, p2))
print(part2(p1, p2))
