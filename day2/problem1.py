import pandas as pd
from collections import defaultdict


def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


def repeats(n):
    def repeatsn(word):
        d = defaultdict(int)
        for c in word:
            d[c] += 1
        return n in d.values()
    return repeatsn


def count(i):
    return sum(1 for e in i)


ids = list(lines('day2/input.txt'))
twos = count(filter(repeats(2), ids))
threes = count(filter(repeats(3), ids))

print(twos)
print(threes)
print(twos * threes)
