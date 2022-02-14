from collections import Counter


with open("./input.txt", "r") as f:
    text = f.read()
    lines = text.splitlines() 
    digits = len(lines[0]) - 1
    nums = [int(line, 2) for line in lines] 

def ratio(nums, f, md): 
    res = 0
    for i in range(md, -1, -1):
        o, z = count_by_index(nums, i)
        if f(o, z) == o:
            res += (1 << i)
    return res

def count_by_index(nums, i):
    total = len(nums)
    res = ones = 0
    for n in nums:            
        if (n >> i) & 1:
            ones += 1    
    return ones, total - ones  

def part1(nums, digits):
    gamma = ratio(nums, max, digits)
    epsilon = ratio(nums, min, digits)
    return gamma * epsilon


def filter_by(nums, f, md):
    n, i = len(nums), md
    while len(nums) > 1 and i >= 0:
        o, z = count_by_index(nums, i)
        s = f(o, z)
        nums = [n for n in nums if ((n >> i) & 1) == s] 
        i -= 1
    return nums.pop()

def part2(nums, digits):
    o2  = filter_by(nums, lambda o, z: 1 if o >= z else 0, digits)
    co2 = filter_by(nums, lambda o, z: 1 if o < z else 0, digits)
    return o2 * co2

print(part1(nums, digits))
print(part2(nums, digits))
