import pandas as pd
import itertools

df = pd.read_csv('input.txt', header=None)
numbers = df[0].tolist()

def repeating_numbers(ns):
    while True:
        for n in ns:
            yield n



def sum_incrementally(ns):
    sum = 0
    #yield sum
    for n in ns:
        sum = sum + n
        yield sum

rep = repeating_numbers(numbers)
sums = sum_incrementally(rep)

seen_freqs= set()
for freq in sums:
    if freq in seen_freqs:
        print(freq)
        break
    else:
        seen_freqs.add(freq)




