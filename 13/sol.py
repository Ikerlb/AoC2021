def parse_fold(f):
    d, fp = f.split("=")                                     
    return (d[-1], int(fp))         

def parse_point(p):
    x, y = p.split(",")    
    return (int(x), int(y))

with open("input.txt", "r") as f:
    txt = f.read()    
    points, folds = txt.split("\n\n")   
    points = {parse_point(p) for p in points.splitlines()}
    folds = [parse_fold(f) for f in folds.splitlines()]

def fold_x(x, points):
    s = set()
    for px, py in points:        
        if px < x:    
            s.add((px, py))        
        else:
            s.add((2 * x - px, py))    
    return s

def fold_y(y, points):
    s = set()    
    for px, py in points:
        if py < y:        
            s.add((px, py))    
        else:
            s.add((px, 2 * y - py))    
    return s

                    
def fold(f, points):
    d, n = f
    if d == "x":        
        return fold_x(n, points)
    return fold_y(n, points)


def format(points):
    mnx = 0
    mxx = max(x for x, _ in points)    
    mny = 0
    mxy = max(y for _, y in points)
    s = []
    for y in range(mny, mxy + 1):
        s.append("".join("#" if (x, y) in points else " " for x in range(mnx, mxx + 1)))    
    return "\n".join(s)

def part1(points, folds):
    return len(fold(folds[0], points))    

def part2(points, folds):
    for f in folds:
        points = fold(f, points)    
    return format(points)
