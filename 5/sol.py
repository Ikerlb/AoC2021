from collections import Counter

def parse_point(s):
    return tuple(int(c) for c in s.split(","))

def parse_line(line):
    return [parse_point(p) for p in line.split(" -> ")]

def delta(n1, n2):
    if (s := n2 - n1) > 0:
        return 1    
    elif s == 0:
        return 0    
    return -1

def span(p1, p2):
    sx, sy = p1 
    ex, ey = p2
    dx = delta(sx, ex)
    dy = delta(sy, ey)
    while p1 != p2:
        yield p1    
        p1 = (p1[0] + dx, p1[1] + dy)
    yield p1

def count_points(segments):
    c = Counter()
    for p1, p2 in segments:
        for p in span(p1, p2):
            c[p] += 1
    return c

with open("input.txt") as f:
    txt = f.read()
    segments = [parse_line(l) for l in txt.splitlines()]

def part1(segments):
    segments = [s for s in segments if s[0][0] == s[1][0] or s[0][1] == s[1][1]]
    c = count_points(segments)
    return sum(1 for v in c.values() if v > 1)
    
def part2(segments):
    c = count_points(segments)
    return sum(1 for v in c.values() if v > 1)

print(part1(segments))
print(part2(segments))
