def get_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    final_list = []
    for line in lines:
        stripped_lines = line.strip()
        str_list = list(stripped_lines)
        line_list = [int(x) for x in str_list]
        final_list.append(line_list)
    print(final_list)
    return final_list

def risk_sum(lowpoint_list):
    return sum(lowpoint_list)+len(lowpoint_list)

def find_lowpoints(point_matrix):
    lowpoints=[]
    for i in range(len(point_matrix)):
        for j in range(len(point_matrix[i])):
            current_point = point_matrix[i][j]
            if i==0 and j==0: #top left corner
               if current_point < point_matrix[i][j+1] and current_point < point_matrix[i+1][j]:
                   lowpoints.append(current_point)
            if i == 0 and j == len(point_matrix[i])-1: #top right corner
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j]:
                    lowpoints.append(current_point)
            if j == 0 and i == len(point_matrix)-1: #bottom left corner
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j]:
                    lowpoints.append(current_point)
            if i == len(point_matrix)-1 and j == len(point_matrix[i])-1: #bottom right corner
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j]:
                    lowpoints.append(current_point)

            if i==0: #top line
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j] and current_point<point_matrix[i][j-1]:
                    lowpoints.append(current_point)
            if j==0: #left line
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j] and current_point<point_matrix[i-1][j]:
                    lowpoints.append(current_point)
            if i==len(point_matrix)-1: #bottom line
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i - 1][j] and current_point<point_matrix[i][j-1]:
                    lowpoints.append(current_point)
            if j==len(point_matrix[i])-1: #right line
                if current_point < point_matrix[i+1][j] and current_point < point_matrix[i - 1][j] and current_point<point_matrix[i][j-1]:
                    lowpoints.append(current_point)


l = get_input()
find_lowpoints(l)
