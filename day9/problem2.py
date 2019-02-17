import re
from collections import defaultdict, deque
from itertools import cycle

with open('day9/input.txt', 'r') as f:
    players_num, last_marble = map(int, re.match("(\d+) players; last marble is worth (\d+) points", f.read()).groups())

last_marble *= 100

def place_marble(circle, marble):
    if marble % 23 == 0:
        circle.rotate(7)
        removed = circle.pop()
        circle.rotate(-1)
        return marble + removed
    else:
        circle.rotate(-1)
        circle.append(marble)
        return 0

def print_marbles(circle):
    current = circle.pop()
    print(*circle, sep=' ', end=' ')
    print("(", current, ")", sep='')
    circle.append(current)

#players_num = 9
#last_marble = 25

players = cycle(range(players_num))
player_scores = defaultdict(int)
marbles = iter(range(last_marble+1))
circle = deque([next(marbles)])
for marble in marbles:
    player = next(players)
    player_scores[player] += place_marble(circle, marble)
    #print_marbles(circle)


print(max(player_scores.values()))
#434674