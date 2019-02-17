import re
from collections import defaultdict

def parse_plants(str):
    return list(map(lambda c: c == '#', str))

def parse_state(str):
    pots = parse_plants(re.match("initial state: ([#.]*)", str).groups()[0])
    return {index for index, hasplant in enumerate(pots) if hasplant}

def parse_rule(str):
    before, after = map(parse_plants, re.match("([#.]*) => ([#.])", str).groups())
    return tuple(before), after[0]

def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def read_input(filename):
    lines = read_lines(filename)
    state = parse_state(next(lines))
    next(lines)
    rules = {before for before, after in map(parse_rule, lines) if after}
    return state, rules

def next_state(state, rules):
    first = min(state)
    last = max(state)
    new_state = set()
    for i in range(first - 2, last + 2):
        if (i-2 in state, i-1 in state, i in state, i+1 in state, i+2 in state) in rules:
            new_state.add(i)
    return new_state

def print_state(state):
    first = -10
    last = max(state)
    print(*['#' if i in state else '-' for i in range(first,last+1)], sep='')



#state, rules = read_input('day12/example.txt')
state, rules = read_input('day12/input.txt')

i = 0

while i < 1000:
    state = next_state(state, rules)
    i += 1

s = sum(state)
print(i, s)

while i < 1010:
    state = next_state(state, rules)
    i += 1
    increment = sum(state) - s
    s += increment
    print(i, s, increment)

generations_left = 50000000000 - i
print(50000000000, s + increment * generations_left)
