# TODO: improve this.
# I do like how _eval came out though
from functools import reduce

class Packet:
    def __init__(self, v, tid, cnt, end):
        self.version = v    
        self.tid = tid
        if self.tid == 4:
            self.v = cnt    
        else:
            self.children = cnt 
        self.end = end

    def __repr__(self):
        if self.tid == 4:    
            return f"version={self.version} value={self.v}"
        return f"version={self.version} children={self.children}" 


def bin_base(s, base):
    i = int(s, base)    
    b = bin(i)[2:]
    return f"{b:>04}"

with open("input.txt", "r") as f:
    hds = f.read().splitlines()[0]
    bits = [bin_base(hd, 16) for hd in hds] 
    bits = "".join(bits)

# ew
def decode(bits, i):
    vn  = int(bits[i:i + 3], 2)
    i += 3
    tid = int(bits[i:i + 3], 2)  
    i += 3
    if tid == 4:
        n = []
        while bits[i] != "0":                    
            n.extend(bits[i + 1: i + 5])
            i += 5
        n.extend(bits[i + 1: i + 5]) 
        return Packet(vn, tid, int("".join(n), 2), i+5) 
    elif bits[i] == "0":
        children = []
        i += 1    
        bl = int(bits[i:i + 15], 2)
        i += 15 
        end = i + bl
        while (pchld := decode(bits, i)).end < end: 
            children.append(pchld) 
            i = pchld.end
        i = pchld.end
        children.append(pchld)
        return Packet(vn, tid, children, i)
    else:
        children = []
        i += 1    
        nsp = int(bits[i:i + 11], 2)
        i += 11 
        for _ in range(nsp):
            pchld = decode(bits, i) 
            children.append(pchld)
            i = pchld.end
        return Packet(vn, tid, children, i)

def versions(n):
    if n.tid == 4:    
        return n.version
    return n.version + sum(versions(nn) for nn in n.children)

def prod(i):
    return reduce(lambda x, y: x * y, i, 1)    

def _eval(node):
    if node.tid == 4:   
        return node.v
    elif node.tid == 0:   
        return sum(_eval(nn) for nn in node.children)
    elif node.tid == 1:
        return prod(_eval(nn) for nn in node.children)
    elif node.tid == 2:
        return min(_eval(nn) for nn in node.children)
    elif node.tid == 3:
        return max(_eval(nn) for nn in node.children)
    elif node.tid == 5:
        n1, n2 = map(_eval, node.children)
        return 1 if n1 > n2 else 0
    elif node.tid == 6:
        n1, n2 = map(_eval, node.children)
        return 1 if n1 < n2 else 0
    elif node.tid == 7:
        n1, n2 = map(_eval, node.children)
        return 1 if n1 == n2 else 0

def part1(bits):
    node = decode(bits, 0)            
    return versions(node)

def part2(bits):
    node = decode(bits, 0)    
    return _eval(node)

print(part1(bits))
print(part2(bits))
