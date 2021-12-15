from operator import itemgetter


def read_input(): #this function is a mess must be cleaned
    input_file = open("input", "r")
    chosen_numbers = []
    lines = input_file.readlines()
    first_line = lines[0]
    first_line = first_line.split(",")
    first_line = [int(l) for l in first_line]
    chosen_numbers.append(first_line)
    for line in lines[1:]: #maybe add line.split() ?
        stripped_line = line.strip()
        stripped_line = stripped_line.split(" ")
        if stripped_line != ['']:
            stripped_line = [int(l) for l in stripped_line if l != ""]
        chosen_numbers.append(stripped_line)
    return chosen_numbers


# def check_if_won(board):
#     for i in range(5):
#         if board[i] == ['X', 'X', 'X', 'X', 'X']:
#             return True
#         col = [sub[i] for sub in board]
#         print(col)
#         if col == ['X', 'X', 'X', 'X', 'X']:
#             return True
#     return False


def check_if_won_flattened_list(flat_board):
    for i in range(5):
        if flat_board[i*5:5*i+5] == ['X', 'X', 'X', 'X', 'X']:
            return True
        col = [flat_board[x * 5 + i] for x in range(5)]
        if col == ['X', 'X', 'X', 'X', 'X']:
            return True
    return False


def get_board_score(flat_board, num):
    no_x_board = [x for x in flat_board if x != 'X']
    return sum(no_x_board) * num


def complete_chosen_numbers_in_board(guessing_numbers, board):  # something here doesnt work
    flat_board = [item for sublist in board for item in sublist]
    # print(guessing_numbers)
    # print(flat_board)
    for i, num in enumerate(guessing_numbers):
        position = [i for i, e in enumerate(flat_board) if e == num]
        # print(position)
        if not position:
            continue
        flat_board[position[0]] = 'X'
        # print(flat_board)
        # print(flat_board)
        if i > 4:
            if check_if_won_flattened_list(flat_board):
                # print(flat_board)
                score = get_board_score(flat_board, num)
                # print(score)
                return [i, num, score]
    return []


def find_winning_board(chosen_numbers, board_list, last=False):
    score_list = []
    for board in board_list:
        score_list.append(complete_chosen_numbers_in_board(chosen_numbers, board))
    s = sorted(score_list, key=itemgetter(0), reverse=False)

    max_index = -1
    the_tuple = []
    if last:
        for my_l in s:
            if max_index < chosen_numbers.index(my_l[1]):
                max_index = chosen_numbers.index(my_l[1])
                the_tuple = my_l
    print(the_tuple, max_index)
    print(s[0][2])


def parse_list(list):
    # TO DO: make boards numbers
    guessing_numbers = list[0]
    matrixes = []
    for i in range(1, len(list), 6):
        temp = []
        temp.append(list[i + 1])
        temp.append(list[i + 2])
        temp.append(list[i + 3])
        temp.append(list[i + 4])
        temp.append(list[i + 5])
        matrixes.append(temp)
    # print(matrixes)
    return guessing_numbers, matrixes


input_list = read_input()
chosen_nums, boards = parse_list(input_list)
find_winning_board(chosen_nums, boards, last=True)
complete_chosen_numbers_in_board(chosen_nums,boards[0])
