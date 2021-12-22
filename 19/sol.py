from itertools import product
from collections import Counter
from math import inf

class Point:
    def __init__(self, x, y, z):
        self.x = x    
        self.y = y    
        self.z = z    

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)    

    def minus(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)    

    def manhattan_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)    

    def __iter__(self):
        yield self.x    
        yield self.y    
        yield self.z    

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"    

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"    

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


def parse_scanner(s):
    _, s = s.split("---\n")
    res = []
    for line in s.splitlines(): 
        res.append(Point(*map(int, line.split(",")))) 
    return res

with open("input.txt", "r") as f:
    txt = f.read()
    scanners = [parse_scanner(s) for s in txt.split("\n\n")]

def rotations(l):
    yield [Point(x, y, z) for x, y, z in l]
    yield [Point(x, -z, y) for x, y, z in l]
    yield [Point(x, -y, -z) for x, y, z in l]
    yield [Point(x, z, -y) for x, y, z in l]
    yield [Point(-x, -y, z) for x, y, z in l]
    yield [Point(-x, z, y) for x, y, z in l]
    yield [Point(-x, y, -z) for x, y, z in l]
    yield [Point(-x, -z, -y) for x, y, z in l]
    yield [Point(y, z, x) for x, y, z in l]
    yield [Point(y, x, -z) for x, y, z in l]
    yield [Point(y, -z, -x) for x, y, z in l]
    yield [Point(y, -x, z) for x, y, z in l]
    yield [Point(-y, x, z) for x, y, z in l]
    yield [Point(-y, z, -x) for x, y, z in l]
    yield [Point(-y, -x, -z) for x, y, z in l]
    yield [Point(-y, -z, x) for x, y, z in l]
    yield [Point(z, x, y) for x, y, z in l]
    yield [Point(z, y, -x) for x, y, z in l]
    yield [Point(z, -x, -y) for x, y, z in l]
    yield [Point(z, -y, x) for x, y, z in l]
    yield [Point(-z, y, x) for x, y, z in l]
    yield [Point(-z, x, -y) for x, y, z in l]
    yield [Point(-z, -y, -x) for x, y, z in l]
    yield [Point(-z, -x, y) for x, y, z in l]

def overlaps(l1, l2):
    c = Counter(p1.minus(p2) for p1, p2 in product(l1, l2))
    for k, v in c.items():
        if v >= 12:    
            return (k, [p.add(k) for p in l2])

def try_all_rotations(cur, scanners):
    for i, rem_s in enumerate(scanners):    
        for rot in rotations(rem_s):    
            for _, rs in cur:    
                if (r := overlaps(rs, rot)) is not None:    
                    return r[0], r[1], i                

def rotate_scanners(scanners):
    scanners = scanners[:]    
    res = [(Point(0, 0, 0), scanners.pop(0))]

    while scanners:
        if (r:=try_all_rotations(res, scanners)) is not None:
            res.append((r[0], r[1]))    
            scanners.pop(r[2]) 
    return res

def part1(rotated_scanners): 
    c = Counter()
    for _, r in rotated_scanners:
        c.update(r)    
    return len(c)

def part2(rotated_scanners):
    m = -inf
    for i in range(len(rotated_scanners)):        
        for j in range(i + 1, len(rotated_scanners)):    
            d1, _ = rotated_scanners[i]
            d2, _ = rotated_scanners[j]
            m = max(m, d1.manhattan_dist(d2))
    return m                      

rotated_scanners = rotate_scanners(scanners)
print(part1(rotated_scanners))
print(part2(rotated_scanners))
