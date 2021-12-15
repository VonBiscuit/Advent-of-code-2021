from collections import Counter


def make_input_array():
    with open('input.txt') as f:
        string_input = f.readlines()
        for line in string_input:
            input_list = line.strip().split(",")
        # print(input_list)
        final_list  = [int(x) for x in input_list]
        return final_list
    

def determine_fuel_cost(crab_pos,dest):
    return abs(crab_pos-dest)


def determine_fuel_cost_part2(crab_pos,dest):
   n = abs(crab_pos-dest)
   return (n*(n+1))/2


def part1_calculations():
    problem_list = make_input_array()
    counted_list = Counter(problem_list)
    x = counted_list.most_common(len(counted_list))
    fuel_cost = []
    for common_elem in x:
        sum_cost = 0
        for elem in problem_list:
            sum_cost += determine_fuel_cost(elem, common_elem[0])
        # print(sum)
        fuel_cost.append(sum_cost)
    return min(fuel_cost)


def part2_calculations():
    problem_list = make_input_array()
    counted_list = Counter(problem_list)
    x = counted_list.most_common(len(counted_list))
    fuel_cost = []
    for i in range(min(problem_list), max(problem_list)):
        sum_cost = 0
        for elem in problem_list:
            sum_cost += determine_fuel_cost_part2(elem, i)
        # print(sum)
        fuel_cost.append(sum_cost)
    return min(fuel_cost)


print(f'Minimum fuel cost for part 1 is: {part1_calculations()}')
print(f'Minimum cost fuel for part 2 is : {part2_calculations()}')
