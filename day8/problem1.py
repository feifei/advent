
with open('day8/input.txt', 'r') as f:
    input = [int(x) for x in f.read().split()]

#input=[2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def parse_tree(num_children, num_metadata, *remaining_data):
    children = []
    for _ in range(num_children):
        child, remaining_data = parse_tree(*remaining_data)
        children.append(child)
    metadata = remaining_data[0:num_metadata]
    remaining_data = remaining_data[num_metadata:]
    return (children, metadata), remaining_data

def print_tree(children, metadata, level=0):
    indent = ' ' * level
    print(indent, metadata, sep='')
    for child in children:
        print_tree(*child, level=level+1)

def sum_tree(children, metadata):
    return sum(metadata) + sum([sum_tree(*child) for child in children])


tree, remaining_data = parse_tree(*input)
assert len(remaining_data) == 0

print_tree(*tree)
print(sum_tree(*tree))