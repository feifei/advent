import re
import string
from collections import defaultdict


def parse_instruction(instruction):
    return re.match("Step (\w+) must be finished before step (\w+) can begin.", instruction).groups()

def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

next_step_time = 61
step_time = {}
for letter in string.ascii_uppercase:
    step_time[letter] = next_step_time
    next_step_time += 1


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
num_workers = 5
work = {}

iterations = 0
while len(work) > 0 or len(available) > 0:
    # Start new work if we have free workers and available work
    while len(work) < num_workers and len(available) > 0:
        first = min(available)
        available.remove(first)
        work[first] = step_time[first]
    # Do one unit of work
    for step in list(work.keys()):
        work[step] -= 1
        # If a step is done, stop working on it and see if some more steps have become available
        if work[step] == 0:
            del work[step]
            done.append(step)
            for candidate in after_dict[step]:
                if all([req in done for req in before_dict[candidate]]):
                    available += candidate
    iterations += 1

print(*done, sep='')
print(iterations)
