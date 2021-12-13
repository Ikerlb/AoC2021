from math import ceil, floor

with open("input.txt", "r") as f:
    l = [int(n) for n in f.read().split(",")]
    l.sort() 

def median(l):
    return l[len(l) >> 1]

def gauss(n):
    return n * (n + 1) // 2

def cost(l, n, f):
    return sum(f(e, n) for e in l)

def part1(l):
    m = median(l)
    return cost(l, m, lambda x, y: abs(x - y))

def part2(l):
    avg = sum(l) / len(l)
    f = lambda x, y: gauss(abs(x - y))
    return min(cost(l, ceil(avg), f), cost(l, floor(avg), f)) 
            
print(part1(l))
print(part2(l))
