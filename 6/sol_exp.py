# the secret sauce
matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0]]

with open("input.txt", "r") as f:
    txt = f.read()
    v = [0 for _ in range(9)]
    for n in txt.split(","):
        v[int(n)] += 1

# had to look this up xd
def prod(X, Y):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def _pow(m, k):
    if k == 1:
        return m
    elif k % 2 == 0:
        half = _pow(m, k >> 1)
        return prod(half, half)
    else:
        half = _pow(m, k >> 1)
        return prod(half, prod(half, m))

print(sum(prod([v], _pow(matrix, 80))[0]))
print(sum(prod([v], _pow(matrix, 256))[0]))
