with open('day5/input.txt', 'r') as f:
    polymer = list(f.read().strip())


def reacts(a, b):
    return a != b and a.upper() == b.upper()


def remove_opposite_pairs(polymer):
    i = 0
    while i < len(polymer) - 1:
        if reacts(*polymer[i:i+2]):
            del polymer[i:i+2]
            if i > 0:
                i -= 1
        else:
            i += 1

# remove_opposite_pairs(polymer)

print(len(polymer))

# 9348
import string

d = {}
for letter in string.ascii_lowercase:
    polymer_filtered = [c for c in polymer if c != letter and c != letter.upper()]
    remove_opposite_pairs(polymer_filtered)
    d[letter] = len(polymer_filtered)

min_len = min(d.items(), key=lambda item: item[1])

print(min_len)
