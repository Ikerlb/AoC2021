path = "./input.txt"
with open(path, "r") as f:
    l = [int(s) for s in f.read().splitlines()]

def solve(l, k):
    s = sum(l[:k])    
    res = 0
    for i in range(k, len(l)):
        ss = s - l[i - k] + l[i]
        res += s < ss
        s = ss
    return res

print(solve(l, 1))
print(solve(l, 3))

