def read_input():
    input_file  = open("input.txt","r")
    input_coords= []
    for line in input_file:
        stripped_line = line.strip()
        input_coords.append(stripped_line)
    return input_coords


def find_depth_and_horizontal(input_coords):
    horizontal = 0
    depth = 0
    aim = 0
    for movement in input_coords:
        command, units = movement.split()
        units = int(units)
        if command == "forward":
            horizontal += units
            depth += aim*units
        elif command == "up":
            # depth -= units
            aim -= units
        elif command == "down":
            # depth += units
            aim += units
        # print(f"horizontal = {horizontal}, depth = {depth}, aim = {aim}")
    return horizontal * depth


input_coord = read_input()
# print(input_coord)
input_coords = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]
print(find_depth_and_horizontal(input_coord))
