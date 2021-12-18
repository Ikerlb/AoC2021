from math import inf

def sign(x):
    if x < 0:    
        return -1    
    elif x > 0:
        return 1    
    else:
        return 0    

class Point:
    def __init__(self, x, y):    
        self.x = x    
        self.y = y

    def add(self, other):
        self.x += other.x 
        self.y += other.y

    def step(self):
        dx = -sign(self.x)
        dy = -1
        self.x += dx
        self.y += dy

    def in_bounds(self, other):
        return self.x <= other.x and self.y >= other.y    

    def in_target(self, ts, te):
        tsx, tsy = ts    
        tex, tey = te
        return tsx <= self.x <= tex and tsy >= self.y >= tey

    def clone(self):
        return Point(self.x, self.y)    

    def __repr__(self):
        return f"({self.x}, {self.y})"    

    def __iter__(self):
        yield self.x    
        yield self.y    

with open("input.txt","r") as f:
    txt = f.read()    
    x, y = txt.split(", y=")   
    x = x.replace("target area: x=", "")

    xs, xe = sorted(map(int, x.split("..")))
    ys, ye = sorted(map(int, y.split("..")), reverse = True)

    ts = Point(xs, ys) 
    te = Point(xe, ye)

# mutates s and v
def step(s, v):
    s.add(v)    
    v.step()  

def steps(s, v, ts, te):
    my = s.y
    while s.in_bounds(te) and not s.in_target(ts, te): 
        my = max(my, s.y)
        step(s, v)
    return my

def _try(s, v, ts, te):
    s = s.clone()    
    v = v.clone() 
    my = steps(s, v, ts, te)
    if s.in_target(ts, te):
        return my    
    return None

# are there any hard bounds on vx and vy??
def possible_velocities(ts, te):
    mny = min(te.y, ts.y)
    for vx in range(te.x + 2):    
        for vy in range(mny, abs(mny)):    
            yield Point(vx, vy)    
            

def part1(s, ts, te):
    my = -inf 
    for v in possible_velocities(ts, te):
        if (t := _try(s, v, ts, te)) is not None:
            my = max(my, t)
    return my
            

def part2(s, ts, te):
    res = 0
    for v in possible_velocities(ts, te):     
        if _try(s, v, ts, te) is not None:
            res += 1    
    return res

start = Point(0, 0)
print(part1(start, ts, te))
print(part2(start, ts, te))
