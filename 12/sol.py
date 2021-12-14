from collections import defaultdict

with open("input.txt", "r") as f:
    txt = f.read()            
    g = defaultdict(list)  
    for line in txt.splitlines():
        a, b = line.split("-")    
        g[a].append(b)  
        g[b].append(a)

# here's to hoping there
# are no uppercase loops
def dfs1(g, node, visited):
    if node == "end":
        return 1
    res = 0
    for nn in g[node]:    
        if nn.isupper() or nn not in visited:
            visited.add(nn) 
            res += dfs1(g, nn, visited)
            visited.discard(nn)    
    return res

# again hoping there 
# are no uppercase loops
def dfs2(g, node, visited, used):
    if node == "end":        
        return 1
    res = 0
    for nn in g[node]:
        if nn.isupper():    
            res += dfs2(g, nn, visited, used)    
        elif nn in visited and nn != "start" and not used:
            res += dfs2(g, nn, visited, True)
        elif nn not in visited:
            visited.add(nn)
            res += dfs2(g, nn, visited, used)
            visited.discard(nn)
    return res

def part1(g):
    return dfs1(g, "start", {"start"})

def part2(g):
    return dfs2(g, "start", {"start"}, False)

print(part1(g))
print(part2(g))
