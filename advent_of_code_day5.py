def read_input():  # this function is a mess must be cleaned
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    points_list = []
    for line in lines:  # maybe add line.split() ?
        stripped_line = line.strip()
        splitted_line = stripped_line.split(" ")
        l = [splitted_line[0].split(","), splitted_line[2].split(",")]
        final_list = [[int(x) for x in l[0]], [int(x) for x in l[1]]]
        # print(final_list)
        points_list.append(final_list)
        # print(stripped_line.split(" "))
    return points_list


def is_straight(point_set_list):
    if point_set_list[0][0] == point_set_list[1][0] or point_set_list[0][1] == point_set_list[1][1]:
        return True
    return False


def map_points(point_list):
    points_on_map = {}
    for point_set in point_list:
        if is_straight(point_set):
            if point_set[0][0] == point_set[1][0]:  # horizontal
                for i in range(min(point_set[0][1], point_set[1][1]), max(point_set[0][1], point_set[1][1]) + 1):
                    if (point_set[0][0], i) in points_on_map:
                        points_on_map[(point_set[0][0], i)] += 1
                    else:
                        points_on_map[(point_set[0][0], i)] = 1
            else:
                for i in range(min(point_set[0][0], point_set[1][0]), max(point_set[0][0], point_set[1][0]) + 1):
                    if (i, point_set[0][1]) in points_on_map:
                        points_on_map[(i, point_set[0][1])] += 1
                    else:
                        points_on_map[(i, point_set[0][1])] = 1
        # else:
        #     if point_set[0][0] < point_set[1][0] and
        #     if point_set[0][0] < point_set[1][0]: #find lower point /
        #         start_point = point_set[0]
        #         end_point = point_set[1]
        #         while start_point != end_point:
        #             if (start_point[0], start_point[1]) in points_on_map:
        #                 points_on_map[(start_point[0], start_point[1])] += 1
        #             else:
        #                 points_on_map[(start_point[0], start_point[1])] = 1
        #             start_point[0] += 1
        #             start_point[1] += 1


    print(sum(int(i) >= 2 for i in points_on_map.values()))
    # print(points_on_map)


test_point_list = [[0, 5], [0, 9]]
# print(is_straight(test_point_list))
input_list = read_input()
map_points(input_list)
