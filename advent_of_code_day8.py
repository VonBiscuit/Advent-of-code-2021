def get_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    encript = []
    for line in lines:
        stripped_lines = line.strip()
        stripped_lines = stripped_lines.replace(" | ", "|")
        encript.append(stripped_lines.split("|"))
    # print(encript)
    return encript


def find_substring_segments(list, characters):
    for item in list:
        if set(characters).issubset(set(list)) and set(characters) != set(list):
            return item
    return False


def decrypt(digits):
    solved_digits_dict = {}
    solved_digits_dict[1] = list(digits.keys())[list(digits.values()).index(2)]
    solved_digits_dict[7] = list(digits.keys())[list(digits.values()).index(3)]
    solved_digits_dict[4] = list(digits.keys())[list(digits.values()).index(4)]
    solved_digits_dict[8] = list(digits.keys())[list(digits.values()).index(7)]

    l = [key for key, value in digits.items() if find_substring_segments(key.lower(), solved_digits_dict[7])]
    solved_digits_dict[3] = [item for item in l if len(item) == 5][0]
    l = [key for key, value in digits.items() if find_substring_segments(key.lower(), solved_digits_dict[4])]
    solved_digits_dict[9] = [item for item in l if len(item) == 6][0]
    six_list = [k for k, v in digits.items() if v == 6]
    five_list = [k for k, v in digits.items() if v == 5]
    five_list.remove(solved_digits_dict[3])
    six_list.remove(solved_digits_dict[9])
    for fitem in five_list:
        for sitem in six_list:
            if set(list(fitem)).issubset(list(sitem)):
                solved_digits_dict[5] = fitem
                solved_digits_dict[6] = sitem
    five_list.remove(solved_digits_dict[5])
    six_list.remove(solved_digits_dict[6])
    solved_digits_dict[0] = six_list[0]
    solved_digits_dict[2] = five_list[0]
    # print(solved_digits_dict)
    return solved_digits_dict


def part1(encrypted):
    sum_easy_digits = 0
    for line in encrypted:
        # print(line)
        list_of_four_digits = line[1].split(" ")
        # print(list_of_four_digits)
        for item in list_of_four_digits:
            if len(item) == 2 or len(item) == 3 or len(item) == 7 or len(item) == 4:
                sum_easy_digits += 1
    print(sum_easy_digits)


def decrypt_signals(list_of_giberish):
    signals = list_of_giberish[0].split(" ")
    # print(signals)
    signal_dict = {}
    for signal in signals:
        sorted_signal = sorted(signal)
        signal_dict["".join(sorted_signal)] = len(signal)
        # print(f'Signal {signal} has length {len(signal)}')
    solved_digits = decrypt(signal_dict)


    enc_num_list=[]
    numbers_to_decrypt = list_of_giberish[1].split(" ")
    for encrypted_num in numbers_to_decrypt:
        enc_num_list.append("".join(sorted(encrypted_num)))

    # print(enc_num_list)
    number_formed = 1000 * list(solved_digits.keys())[list(solved_digits.values()).index(enc_num_list[0])] + 100 * \
                    list(solved_digits.keys())[list(solved_digits.values()).index(enc_num_list[1])] + 10 * \
                    list(solved_digits.keys())[list(solved_digits.values()).index(enc_num_list[2])] + \
                    list(solved_digits.keys())[list(solved_digits.values()).index(enc_num_list[3])]
    # print(number_formed)
    return number_formed



encrypted_digits = get_input()
# part1(encrypted_digits)
l=[]
for line in encrypted_digits:
    l.append(decrypt_signals(line))

print(sum(l))
