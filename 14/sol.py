from collections import Counter

with open("input.txt", "r") as f:
    txt = f.read()    
    polymer, rules = txt.split("\n\n")
    rules = dict(r.split(" -> ") for r in rules.splitlines())

def count(s, rules, steps):
    c = Counter()
    for i in range(len(s) - 1):
        c[s[i:i + 2]] += 1    

    for _ in range(steps):
        nc = Counter()
        for pp in c:
            if pp in rules:
                res = rules[pp]
                nc[pp[0] + res] += c[pp] 
                nc[res + pp[1]] += c[pp]
        c = nc

    nc = Counter()
    for pp in c:
        nc[pp[0]] += c[pp]      
    nc[s[-1]] += 1             
    sc = sorted(nc.items(), key = lambda x: x[1])
    return sc[-1][1] - sc[0][1]

print(count(polymer, rules, 10))
print(count(polymer, rules, 40))
