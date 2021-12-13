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
def dfs1(g, node, visited, path, res):
    if node == "end":
        res.append(path + ["end"])        
        return
    for nn in g[node]:    
        if nn.isupper() or nn not in visited:
            visited.add(nn) 
            dfs1(g, nn, visited, path + [node], res)
            visited.discard(nn)    

# again hoping there 
# are no uppercase loops
def dfs2(g, node, visited, path, res, used):
    if node == "end":        
        res.append(path + ["end"])    
        return
    for nn in g[node]:
        if nn.isupper():    
            dfs2(g, nn, visited, path + [node], res, used)    
        elif nn in visited and nn != "start" and not used:
            dfs2(g, nn, visited, path + [node], res, True)
        elif nn not in visited:
            visited.add(nn)
            dfs2(g, nn, visited, path + [node], res, used)
            visited.discard(nn)

def part1(g):
    res = []        
    dfs1(g, "start", {"start"}, [], res)
    return len(res)

def part2(g):
    res = []    
    dfs2(g, "start", {"start"}, [], res, False)
    return len(res)
