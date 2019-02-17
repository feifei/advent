import re
from collections import defaultdict
from itertools import cycle

with open('day9/input.txt', 'r') as f:
    players_num, last_marble = map(int, re.match("(\d+) players; last marble is worth (\d+) points", f.read()).groups())

last_marble *= 100


def place_marble(circle, idx, next_marble):
    if next_marble % 23 == 0:
        idx = (idx - 7) % len(circle)
        score = next_marble + circle[idx]
        del circle[idx]
    else:
        idx = (idx + 2) % len(circle)
        score = 0
        circle.insert(idx, next_marble)
    return idx, score

def print_marble(circle, current_marble):
    for marble in circle:
        if marble == current_marble:
            print("(", marble, ") ", sep = "", end="")
        else:
            print(marble, " ", end="")
    print("\n")

#players_num = 9
#last_marble = 25

players = cycle(range(players_num))
player_scores = defaultdict(int)
marbles = iter(range(last_marble+1))
circle = [next(marbles)]
idx = 0
for next_marble in marbles:
    player = next(players)
    idx, score = place_marble(circle, idx, next_marble)
    player_scores[player] += score
    #print_marble(circle, current_marble)


print(max(player_scores.values()))
#434674