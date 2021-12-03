from collections import Counter

with open("./test.txt", "r") as f:
    text = f.read()
    nums = [int(line, 2) for line in text.splitlines()] 

def ratio(ones, f): 
    res = 0
    md = max(ones)
    for i in range(md, -1, -1):    
        o = ones[i]
        z = len(nums) - o
        if f(o, z) == o:
            res += (1 << i)    
    return res

def part1():
    # indices and their # of ones
    ones = Counter()
    for n in nums:
        i = 0
        while n:    
            if n & 1 == 1:
                ones[i] += 1
            n >>= 1    
            i += 1
    # or just get the binary compliment
    # of either one of the other
    # this is cleaner it think
    gamma = ratio(ones, max)
    epsilon = ratio(ones, min)
    return gamma * epsilon

# to do the part 2, kinda tired xd
