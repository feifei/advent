import re
from collections import defaultdict

def parse_instruction(instruction):
    return re.match("Step (\w+) must be finished before step (\w+) can begin.", instruction).groups()

def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

instructions = [parse_instruction(line) for line in lines('day7/input.txt')]

steps = set()
before_dict = defaultdict(list)
after_dict = defaultdict(list)

for before, after in instructions:
    steps.add(before)
    steps.add(after)
    before_dict[after] += before
    after_dict[before] += after

available = [step for step in steps if len(before_dict[step]) == 0]

done = []

while len(available) > 0:
    first = min(available)
    available.remove(first)
    done += first
    for candidate in after_dict[first]:
        if all([req in done for req in before_dict[candidate]]):
            available += candidate

print(*done, sep='')

