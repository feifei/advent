
def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.rstrip()

train_chars = set(['^', 'v', '<', '>', 'X'])

straight_track_chars = set(['|', '-'])
curve_track_chars = set(['/', '\\'])
intersection_track_char = '+'
collision_char = 'X'

direction_after_curve = {
    ('^', '/'): '>',
    ('^', '\\'): '<',
    ('>', '\\'): 'v',
    ('>', '/'): '^',
    ('v', '/'): '<',
    ('v', '\\'): '>',
    ('<', '\\'): '^',
    ('<', '/'): 'v'
}

direction_after_intersection = {
    ('^', 0): ('<', 1),
    ('^', 1): ('^', 2),
    ('^', 2): ('>', 0),
    ('>', 0): ('^', 1),
    ('>', 1): ('>', 2),
    ('>', 2): ('v', 0),
    ('v', 0): ('>', 1),
    ('v', 1): ('v', 2),
    ('v', 2): ('<', 0),
    ('<', 0): ('v', 1),
    ('<', 1): ('<', 2),
    ('<', 2): ('^', 0)
}

track_under_train = {
    '^': '|',
    'v': '|',
    '<': '-',
    '>': '-'
}

def next_direction(direction, memory, track):
    if (track in straight_track_chars):
        return (direction, memory)
    elif (track in curve_track_chars):
        return (direction_after_curve[(direction, track)], memory)
    elif (track == intersection_track_char):
        return direction_after_intersection[(direction, memory)]

def move(coord, direction):
    y, x = coord
    if direction == '^':
        return y-1, x
    elif direction == '>':
        return y, x+1
    elif direction == 'v':
        return y+1, x
    elif direction == '<':
        return y, x-1


def extract_trains(tracks):
    trains = {}
    for y, row in enumerate(tracks):
        for x, char in enumerate(row):
            if char in train_chars:
                trains[(y, x)] = (char, 0)
                tracks[y][x] = track_under_train[char]
    return trains

def read_map(filename):
    tracks = list(map(list, read_lines(filename)))
    trains = extract_trains(tracks)
    return tracks, trains

def print_tracks_and_trains(tracks, trains):
    for y, row in enumerate(tracks):
        for x, char in enumerate(row):
            if (y, x) in trains:
                print(trains[(y,x)][0], sep='', end='')
            else:
                print(tracks[y][x], sep='', end='')
        print()

def sort_trains_by_priority(trains):
    return sorted(trains.items())

def tick(tracks, trains):
    moved_trains = dict()
    for coord, direction_and_memory in sort_trains_by_priority(trains):
        direction, memory = direction_and_memory
        coord = move(coord, direction)
        y, x = coord
        direction, memory = next_direction(direction, memory, tracks[y][x])
        if coord in moved_trains:
            print("Collision at row %d col %d" % (y, x))
            return None
        else:
            moved_trains[coord] = (direction, memory)
    return moved_trains

tracks, trains = read_map('day13/input.txt')
#tracks, trains = read_map('day13/example.txt')
i = 0
while trains is not None:
    #print_tracks_and_trains(tracks, trains)
    #print()
    trains = tick(tracks, trains)
    i += 1

print(i)
