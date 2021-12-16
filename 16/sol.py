# TODO: improve this.
# TODO: Maybe a packet class
# I do like how _eval came out though
from functools import reduce

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
        return (vn, tid, int("".join(n), 2), i + 5)
    elif bits[i] == "0":
        n = []
        i += 1    
        bl = int(bits[i:i + 15], 2)
        i += 15 
        end = i + bl
        while (pchld := decode(bits, i))[-1] < end: 
            n.append(pchld) 
            i = pchld[-1] 
        i = pchld[-1]
        n.append(pchld)
        return (vn, tid, n, i)
    else:
        n = []
        i += 1    
        nsp = int(bits[i:i + 11], 2)
        i += 11 
        for _ in range(nsp):
            pchld = decode(bits, i)                
            n.append(pchld)
            i = pchld[-1] 
        return (vn, tid, n, i)

def versions(node): 
    if node[1] == 4: 
        return node[0]    
    return node[0] + sum(versions(nn) for nn in node[2])

def prod(i):
    return reduce(lambda x, y: x * y, i, 1)    

def _eval(node):
    if node[1] == 4:   
        return node[2]    
    elif node[1] == 0:   
        return sum(_eval(nn) for nn in node[2])     
    elif node[1] == 1:
        return prod(_eval(nn) for nn in node[2])
    elif node[1] == 2:
        return min(_eval(nn) for nn in node[2])    
    elif node[1] == 3:
        return max(_eval(nn) for nn in node[2])    
    elif node[1] == 5:
        n1, n2 = map(_eval, node[2])
        return 1 if n1 > n2 else 0      
    elif node[1] == 6:
        n1, n2 = map(_eval, node[2])
        return 1 if n1 < n2 else 0      
    elif node[1] == 7:
        n1, n2 = map(_eval, node[2])
        return 1 if n1 == n2 else 0      

def part1(bits):
    node = decode(bits, 0)            
    return versions(node)

