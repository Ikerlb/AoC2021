from math import inf

class SnailfishNumber:
    # leaves should have val = None
    def __init__(self, l=None, r=None, p=None, v=None):
        self.l = l 
        self.r = r 
        self.val = v
        self.parent = p

    def __repr__(self):
        if self.val is not None:            
            return str(self.val)    
        return f"[{self.l},{self.r}]"

    def clone(self):
        if self.val is not None:    
            return SnailfishNumber(v = self.val)
        l = self.l.clone()
        r = self.r.clone()
        nn = SnailfishNumber(l, r)
        l.parent = r.parent = nn
        return nn

def parse(s, i):
    if s[i].isdigit():
        return (SnailfishNumber(v = int(s[i])), i + 1)
    l, li = parse(s, i + 1) 
    r, ri = parse(s, li + 1)
    n = SnailfishNumber(l, r)
    l.parent = r.parent = n
    return n, ri + 1

with open("input.txt") as f:
    txt = f.read()
    nums = [parse(line, 0)[0] for line in txt.splitlines()]

def leftmost(n):
    if n.val is not None:    
        return n    
    return leftmost(n.l)
        
def rightmost(n):
    if n.val is not None:    
        return n    
    return rightmost(n.r)

def _next(n):
    p = n
    while p.parent and p.parent.r == p:
        p = p.parent    
    if not p.parent or p.parent.r == p: # no next elem
        return None            
    return leftmost(p.parent.r)

# underscore for consistency
def _prev(n):
    p = n    
    while p.parent and p.parent.l == p:
        p = p.parent    
    if not p.parent or p.parent.l == p:
        return None    
    return rightmost(p.parent.l)

# there should be no case where
# we have nodes with d > 4
def explode(n, d):
    if d == 4 and n.l and n.l.val is not None and n.r and n.r.val is not None:
        if (pn := _prev(n)) is not None:        
            pn.val += n.l.val
        if (nn := _next(n)) is not None:
            nn.val += n.r.val    
        n.l = n.r = None
        n.val = 0
        return True
    if n.val is not None or d >= 4:
        return False    
    return explode(n.l, d + 1) or explode(n.r, d + 1)

def split(n):
    if n.val is not None and n.val > 9:
        nn, n.val = n.val, None        
        d, m = divmod(nn, 2)
        n.l = SnailfishNumber(v = d, p = n)  
        n.r = SnailfishNumber(v = (d + m), p = n)
        return True
    elif n.val is not None:
        return False    
    return split(n.l) or split(n.r)

# mutates root
def reduce(root):
    while explode(root, 0) or split(root):        
        pass    

# POP POP amirite?
def magnitude(n):
    if n.val is not None:            
        return n.val    
    return 3 * magnitude(n.l) + 2 * magnitude(n.r)

def _sum(nums):
    g = iter(nums)
    prev = next(g)
    while (nxt := next(g, None)):
        nn = SnailfishNumber(prev, nxt)
        prev.parent = nxt.parent = nn 
        reduce(nn)
        prev = nn
    return prev

def part1(nums):
    nums = [n.clone() for n in nums]
    return magnitude(_sum(nums))

def part2(nums):
    m = -inf
    for i in range(len(nums)):            
        for j in range(len(nums)):    
            if i == j:    
                continue    
            n = _sum([nums[i].clone(), nums[j].clone()])
            m = max(m, magnitude(n))
    return m

print(part1(nums))
print(part2(nums))
