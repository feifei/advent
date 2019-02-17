with open('day5/input.txt', 'r') as f:
    polymer = f.read().strip()


def repeat_until_fixed(input, function):
    output = function(input)
    if output == input:
        return output
    else:
        return repeat_until_fixed(output, function)


def remove_opposite_pairs(str):
    if len(str) < 2:
        return str
    elif str[0] != str[1] and str[0].upper() == str[1].upper():
        return remove_opposite_pairs(str[2:])
    else:
        return str[0] + remove_opposite_pairs(str[1:])




def repeat_until_fixed2(first_input, function):
    prev_input = None
    next_input = first_input
    while next_input != prev_input:
        prev_input = next_input
        next_input = function(next_input)
    return next_input


def remove_opposite_pairs2(polymer):
    i = 0
    polymer_removed = ""
    while i < len(polymer) :
        first = polymer[i]
        if i == len(polymer) - 1:
            polymer_removed += first
            i += 1
        else:
            second = polymer[i+1]
            if first != second and first.upper() == second.upper():
                i += 2
            else:
                polymer_removed += first
                i += 1
    return polymer_removed



print(len(repeat_until_fixed2(polymer, remove_opposite_pairs2)))

# 9348