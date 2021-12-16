import numpy as np
import queue

def get_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    final_list = []
    for line in lines:
        stripped_lines = line.strip()
        str_list = list(stripped_lines)
        line_list = [int(x) for x in str_list]
        final_list.append(line_list)
    # print(final_list)
    return final_list


def risk_sum(lowpoint_list):
    return sum(lowpoint_list) + len(lowpoint_list)


def find_lowpoints(point_matrix):
    lowpoints = []
    lowpoints_indices=[]
    for i in range(len(point_matrix)):
        for j in range(len(point_matrix[i])):
            current_point = point_matrix[i][j]
            if i == 0 and j == 0:  # top left corner
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))
            elif i == 0 and j == len(point_matrix[i]) - 1:  # top right corner
                if current_point < point_matrix[i][j - 1] and current_point < point_matrix[i + 1][j]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))
            elif j == 0 and i == len(point_matrix) - 1:  # bottom left corner
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i - 1][j]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))
            elif i == len(point_matrix) - 1 and j == len(point_matrix[i]) - 1:  # bottom right corner
                if current_point < point_matrix[i][j - 1] and current_point < point_matrix[i - 1][j]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))

            elif i == 0:  # top line
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j] and current_point < \
                        point_matrix[i][j - 1]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))
            elif j == 0:  # left line
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j] and current_point < \
                        point_matrix[i - 1][j]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))
            elif i == len(point_matrix) - 1:  # bottom line
                if current_point < point_matrix[i][j + 1] and current_point < point_matrix[i - 1][j] and current_point < \
                        point_matrix[i][j - 1]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))
            elif j == len(point_matrix[i]) - 1:  # right line
                if current_point < point_matrix[i + 1][j] and current_point < point_matrix[i - 1][j] and current_point < \
                        point_matrix[i][j - 1]:
                    lowpoints.append(current_point)
                    lowpoints_indices.append((i,j))

            elif current_point < point_matrix[i][j - 1] and current_point < point_matrix[i - 1][j] and current_point < \
                    point_matrix[i][j + 1] and current_point < point_matrix[i + 1][j]:
                lowpoints.append(current_point)
    # print(lowpoints)
    print(risk_sum(lowpoints))
    return lowpoints_indices


def bfs(queue=None):
    current_index = queue.get()
    current_x, current_y = current_index[0], current_index[1]

    element = matrix[current_x,current_y]

    # if element == 1:
    #     return current_x, current_y

    for n in range(current_x - 1, current_x + 2):
        for m in range(current_y - 1, current_y + 2):
            if not (n == current_x and m == current_y) \
                    and n > -1 and m > -1 \
                    and n < matrix.shape[0] and m < matrix.shape[1] \
                    and (n,m) not in queue.queue:
                queue.put((n, m))
    print(queue)
    return bfs(queue)


l = get_input()
matrix = np.array(l)
# print(matrix)
q=queue.Queue()
q.put((0,1))
# bfs(q)
# find_lowpoints(l)
