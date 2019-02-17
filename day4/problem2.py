from collections import defaultdict
import re
import pandas as pd

def lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

log_lines = sorted(lines('day4/input.txt'))

guards = defaultdict(lambda: defaultdict(int))
guard = None
sleep_start = None
for log_line in log_lines:
    newshift = re.search("Guard #(\d+)", log_line)
    asleep = re.search("00:(\d+)] falls asleep", log_line)
    awake = re.search("00:(\d+)] wakes up", log_line)
    if newshift:
        assert sleep_start is None
        guard = int(newshift.groups()[0])
    elif asleep:
        sleep_start = int(asleep.groups()[0])
    elif awake:
        sleep_end = int(awake.groups()[0])
        for minute in range(sleep_start, sleep_end):
            guards[guard][minute] += 1
        sleep_start = None


def sleep_counts(guards):
    for guard in guards:
        for minute in guards[guard]:
            yield (guard, minute, guards[guard][minute])

guard_sleep_counts = list(sleep_counts(guards))

sleepiest_minute = max(guard_sleep_counts, key=lambda item: item[2])

print(sleepiest_minute[0] * sleepiest_minute[1])
