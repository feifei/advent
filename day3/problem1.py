from collections import defaultdict
import re

def parse_claim(claim):
    # 1 @ 287,428: 27x20
    return [int(x) for x in re.match("#\d+ @ (\d+),(\d+): (\d+)x(\d+)", claim).groups()]

def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def claimed_squares(x, y, width, height):
    for i in range(x, x+width):
        for j in range(y, y+height):
            yield (i, j)

claims = [parse_claim(line) for line in lines('day3/input.txt')]

all_claimed_squares = set()
overclaimed_squares = set()
for claim in claims:
    new_suqares = set(claimed_squares(*claim))
    overlapping = all_claimed_squares & new_suqares
    all_claimed_squares.update(new_suqares)
    overclaimed_squares.update(overlapping)

print(len(overclaimed_squares))



