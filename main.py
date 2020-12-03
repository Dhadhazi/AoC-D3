with open("input.txt") as file:
    map_lines = file.read().splitlines()

line_base_length = len(map_lines[0])


def way_tree_counter(right, down):
    number_of_trees = 0
    for i in range(0, int(len(map_lines)/down)):
        step = i * right
        if map_lines[i*down][step % line_base_length] == "#":
            number_of_trees += 1
    return number_of_trees


# PART ONE

print(f"Part one solution (right 3, down 1): {way_tree_counter(3, 1)}")

# PART TWO
ways = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

multiplied_tree_counter = 1

for way in ways:
    multiplied_tree_counter *= way_tree_counter(way[0], way[1])

print(f"Part two solution: {multiplied_tree_counter}")