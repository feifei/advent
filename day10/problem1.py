import re

def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def parse_line(line):
    x, y, dx, dy = map(int, re.match("position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d+),  ?(-?\d+)>", line).groups())
    return (x, y), (dx, dy)

def step(pos, speed, t):
    x, y = pos
    dx, dy = speed
    return x + (t * dx), y + (t * dy)

def stepall(points, t):
    return [step(pos, speed, t) for pos, speed in points]

def bounding_limits(points):
    min_x = min([x for (x, y) in points])
    max_x = max([x for (x, y) in points])
    min_y = min([y for (x, y) in points])
    max_y = max([y for (x, y) in points])
    return min_x, max_x, min_y, max_y

def bounding_size(points):
    min_x, max_x, min_y, max_y = bounding_limits(points)
    return (max_x - min_x) * (max_y - min_y)

def print_points(points):
    min_x, max_x, min_y, max_y = bounding_limits(points)
    pointset = set(points)
    for y in range(min_y, max_y + 1):
        print(*[('·' if (x, y) in pointset else ' ') for x in range(min_x, max_x + 1)], sep=' ')


initial = [parse_line(line) for line in read_lines('day10/input.txt')]

meeting_t = min(range(10000, 11000), key=lambda t: bounding_size(stepall(initial, t)))
print(meeting_t)
print()

print_points(stepall(initial, meeting_t))
