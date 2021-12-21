from itertools import product
from math import inf
from collections import defaultdict

with open("input.txt", "r") as f:
    txt = f.read()    
    algo, img = txt.split("\n\n") 
    img = img.splitlines()
    lit = defaultdict(lambda: ".")
    for r in range(len(img)):
        for c in range(len(img[r])):   
            if img[r][c] == "#":
                lit[r, c] = "#"        

def show(lit):
    mnr = min(r for r, c in lit)            
    mxr = max(r for r, c in lit)
    mnc = min(c for r, c in lit)            
    mxc = max(c for r, c in lit)
    
    res = []
    for r in range(mnr - 2, mxr + 3): 
        res.append("".join(lit[r, c] for c in range(mnc - 2, mxc + 3)))
    return "\n".join(res)
       
    
def enhance_pixel(lit, algo, r, c):
    encoding = 0
    for dr, dc in product(range(-1, 2), repeat = 2):    
        encoding <<= 1 
        if lit[r+dr, c+dc] == "#":
            encoding += 1
    return algo[encoding]

def bounds(lit):
    mnr = min(r for r, c in lit)            
    mxr = max(r for r, c in lit)
    mnc = min(c for r, c in lit)            
    mxc = max(c for r, c in lit)
    return mnr, mxr, mnc, mxc

# there is a special case
# that comes when algo[0]
# is #, that is the infinite
# grid will be turning
# on and off
# we have to account for this!!
def enhance(lit, algo, infinity):
    mnr, mxr, mnc, mxc = bounds(lit)

    nlit = defaultdict(lambda: infinity)
    for r in range(mnr - 2, mxr + 3):
        for c in range(mnc - 2, mxc + 3):
            nlit[r, c] = enhance_pixel(lit, algo, r, c)
    return nlit

def steps(lit, algo, n):
    infinity = "."
    for i in range(n):
        infinity = algo[0] if infinity == "." else algo[-1]
        lit = enhance(lit, algo, infinity)
    return lit 

def part1(lit, algo):
    lit = steps(lit, algo, 2)
    return sum(1 for v in lit.values() if v == "#")

def part2(lit, algo):
    lit = steps(lit, algo, 50)            
    return sum(1 for v in lit.values() if v == "#")

print(part1(lit, algo))
print(part2(lit, algo))
