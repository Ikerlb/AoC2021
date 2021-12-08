from collections import defaultdict
from itertools import permutations

def parse(line):
    signals_s, displays_s = line.split(" | ")
    signals = [s for s in signals_s.split(" ")]
    displays = [s for s in displays_s.split(" ")]  
    return signals, displays

with open("input.txt", "r") as f:
    entries = [parse(l) for l in f.read().splitlines()]    

def part1(entries):
    return sum(1 for _, ds in entries for d in ds if len(d) in [2, 3, 4, 7])

num2segments = {
    0: {0, 1, 2, 4, 5, 6}, 
    1: {2, 5},
    2: {0, 2, 3, 4, 6},
    3: {0, 2, 3, 5, 6},
    4: {1, 2, 3, 5},
    5: {0, 1, 3, 5, 6},
    6: {0, 1, 3, 4, 5, 6},
    7: {0, 2, 5}, 
    8: {0, 1, 2, 3, 4, 5, 6}, 
    9: {0, 1, 2, 3, 5, 6},
}

segments2nums = {tuple(sorted(v)):k for k, v in num2segments.items()}

lengths = defaultdict(list)
for k, l in num2segments.items():
    lengths[len(l)].append(k)    

def try_signal(signal, guess, permutation):
    return all(permutation[c] in num2segments[guess] for c in signal)    

def try_guesses(signal, permutation):
    return any(try_signal(signal, g, permutation) for g in lengths[len(signal)])    

def try_permutations(signals):
    for p in permutations("abcdefg"):    
        pd = {p[i]:i for i in range(len(p))}    
        if all(try_guesses(s, pd) for s in signals):    
            return p    

def decode(display, permutation):
    n = segments2nums[tuple(sorted(permutation.index(c) for c in display))]
    return int(n)
    
def part2(entries):
    res = 0
    for s, ds in entries:    
        p = try_permutations(s)
        n = 0
        for d in ds:
            n += decode(d, p)
            n *= 10
        res += n // 10
    return res
                  
print(part1(entries))
print(part2(entries))
