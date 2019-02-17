import re
from collections import defaultdict
from itertools import cycle

with open('day9/input.txt', 'r') as f:
    players_num, last_marble = map(int, re.match("(\d+) players; last marble is worth (\d+) points", f.read()).groups())

def place_marble(circle, current_marble, next_marble):
    idx = circle.index(current_marble)

    if next_marble % 23 == 0:
        removed_marble = circle[idx - 7]
        new_current_marble = circle[idx - 6]
        circle.remove(removed_marble)
        score = next_marble + removed_marble
    else:
        circle.insert((idx + 2) % len(circle), next_marble)
        new_current_marble = next_marble
        score = 0

    return circle, new_current_marble, score

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
current_marble = circle[0]
for next_marble in marbles:
    player = next(players)
    circle, current_marble, score = place_marble(circle, current_marble, next_marble)
    player_scores[player] += score
    #print_marble(circle, current_marble)


print(max(player_scores.values()))