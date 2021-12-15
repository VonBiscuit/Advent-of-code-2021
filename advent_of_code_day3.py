# input_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
#               '01010']
global frequency_dict;
frequency_dict = {
    0: {0: 0, 1: 0},
    1: {0: 0, 1: 0},
    2: {0: 0, 1: 0},
    3: {0: 0, 1: 0},
    4: {0: 0, 1: 0},
    5: {0: 0, 1: 0},
    6: {0: 0, 1: 0},
    7: {0: 0, 1: 0},
    8: {0: 0, 1: 0},
    9: {0: 0, 1: 0},
    10: {0: 0, 1: 0},
    11: {0: 0, 1: 0}
}


def read_input():
    input_file = open("input.txt", "r")
    input_list = []
    for line in input_file:
        stripped_line = line.strip()
        input_list.append(stripped_line)
    return input_list


input_list = read_input()


#
# def break_bits_apart(bit_sequence):
#     bitlist = [int(a) for a in str(bit_sequence)]
#     for i, b in enumerate(bitlist):
#         frequency_dict[i][b] += 1
#     return frequency_dict
#
#
# for val in input_list:
#     break_bits_apart(val)
#
# l = []
# for k, v in frequency_dict.items():
#     if frequency_dict[k][0] >= frequency_dict[k][1]:
#         l.append('0')
#     else:
#         l.append('1')
#


# str_bits = "".join(l)
# temp = bin(int(str_bits,2))
# complement_val = 0b111111111111 - int(str_bits,2)
# print(int(str_bits,2)*complement_val)

def determine_bit_frequency_by_position(pos, bitlist):
    bit_frequency = {0: 0, 1: 0}
    for val in bitlist:
        bit_frequency[int(val[pos])] += 1
    return bit_frequency


def oxygen_generator_rating(input_list):
    bit_criteria_list = input_list
    bit_frequency = {}
    for pos in range(12):
        if len(bit_criteria_list) == 1:
            break
        bit_frequency = determine_bit_frequency_by_position(pos, bit_criteria_list)
        if bit_frequency[0] == bit_frequency[1]:
            most_frequent_bit = '1'
        else:
            most_frequent_bit = str(max(bit_frequency, key=bit_frequency.get))
        bit_criteria_list = list(filter(lambda x: x[pos] == most_frequent_bit, bit_criteria_list))
    return bit_criteria_list


def co2_scrubber_rating(input_list):
    bit_criteria_list = input_list
    bit_frequency = {}
    for pos in range(12):
        if len(bit_criteria_list) == 1:
            break
        bit_frequency = determine_bit_frequency_by_position(pos, bit_criteria_list)
        if bit_frequency[0] == bit_frequency[1]:
            least_frequent_bit = '0'
        else:
            least_frequent_bit = str(min(bit_frequency, key=bit_frequency.get))
        bit_criteria_list = list(filter(lambda x: x[pos] == least_frequent_bit, bit_criteria_list))
    return bit_criteria_list


o = oxygen_generator_rating(input_list)
c = co2_scrubber_rating(input_list)
print(o, c)
print(int(o[0], 2) * int(c[0], 2))
