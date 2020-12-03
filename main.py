with open("input.txt") as file:
    map_lines = file.read().splitlines()

line_base_length = len(map_lines[0])
number_of_trees = 0

for i in range(1, len(map_lines)):
    step = i*3
    if map_lines[i][step % line_base_length] == "#":
        number_of_trees += 1

print(number_of_trees)