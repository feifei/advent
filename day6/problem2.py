def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def parse_coordinate(line):
    return tuple(int(i) for i in line.split(', '))

coordinates = [parse_coordinate(line) for line in lines('day6/input.txt')]


def cal_distance(coord, square):
    x, y = coord
    square_x, square_y = square
    return abs(x - square_x) + abs(y - square_y)

def sum_distance(coord, assigned_squares):
    tot_distance = 0
    for square in assigned_squares:
        tot_distance += cal_distance(coord, square)
    return tot_distance

def limits(coordinates):
    min_x = min([x for (x, y) in coordinates])
    max_x = max([x for (x, y) in coordinates])
    min_y = min([y for (x, y) in coordinates])
    max_y = max([y for (x, y) in coordinates])
    return min_x, max_x, min_y, max_y


n = 0
min_x, max_x, min_y, max_y = limits(coordinates)
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if sum_distance((x,y), coordinates) < 10000:
            n += 1

print(n)
