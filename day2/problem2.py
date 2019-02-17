
def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

ids = list(lines('day2/input.txt'))

for left in ids:
    for right in ids:
        if sum([1 for l, r in zip(left, right) if l != r]) == 1:
            print(''.join([l for l, r in zip(left, right) if l == r]))
