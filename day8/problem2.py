
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

def tree_value(children, metadata):
    if len(children) > 0:
        child_values = {i+1: tree_value(*child) for i, child in enumerate(children)}
        return sum([child_values[i] for i in metadata if i in child_values])
    else:
        return sum(metadata)

tree, remaining_data = parse_tree(*input)
assert len(remaining_data) == 0
print(tree_value(*tree))
