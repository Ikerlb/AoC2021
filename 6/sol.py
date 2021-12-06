from collections import deque, Counter

with open("input.txt", "r") as f:
    txt = f.read()
    c = Counter(int(n) for n in txt.split(","))

# mutates q
def step(q):
    n, last = q[0], q.pop()    
    q[-1] += n
    q.append(last)
    q.rotate(-1)

def steps(c, days):
    q = deque(c[i] for i in range(9))
    for _ in range(days): 
        step(q)    
    return sum(q) 

print(steps(c, 80))
print(steps(c, 256))
