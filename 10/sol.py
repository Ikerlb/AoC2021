with open("input.txt", "r") as f:
    txt = f.read()    
    lines = list(txt.splitlines())      

m = {"{":"}", "(":")", "[":"]", "<":">"}

def parse(l):
    s = []
    for c in l:
        if c in "{(<[":    
            s.append(c)    
        elif s and m[s[-1]] == c:
            s.pop()
        else:
            return s, c
    return s, None

def part1(lines):
    s = 0
    mm = {")":3, "]":57, "}":1197, ">":25137}
    for l in lines:
        _, i = parse(l)    
        if i is None:  
            continue    
        else:
            s += mm[i]    
    return s

def part2(lines):
    sl = []
    mm = {"(":1, "[":2, "{":3, "<":4}
    for l in lines:
        s, i = parse(l)
        if i is not None:    
            continue    
        rr = 0
        for c in reversed(s): 
            rr *= 5
            rr += mm[c]
        sl.append(rr)
    return sorted(sl)[len(sl) >> 1]

print(part1(lines))
print(part2(lines))
