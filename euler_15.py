"""Starting in the top left corner of a 2×2 grid there are 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """
import pandas as pd
from numpy import prod

MATRIX = [[True, False, False, False],
          [False, False, False, False],
          [False, False, False, False],
          [False, False, False, False]]


def get_next_step(matrix_in):
    """Identify the next legal moves that can be made from a given state."""
    matrix_df = matrix_in
    row = matrix_df.iloc[0]
    column = matrix_df[0]
    max_row = list()
    max_column = list()
    for row in range(len(column)):
        for column in range(len(row)):
            if matrix_df.iat(row, column):
                max_row.append(row)
                max_column.append(column)
    if max(max_row) + 1 <= len(row):
        down_move = [max(max_row) + 1, max(max_column)]
    else:
        down_move = [0]
    if max(max_column) + 1 <= len(column):
        right_move = [max(max_row), max(max_column) + 1]
    else:
        right_move = [0]
    route_length = max([sum(down_move), sum(right_move)])
    return down_move, right_move, route_length


def get_route(in_matrix):
    """Carries out the moves dictated in get_next_step."""
    moves = get_next_step(in_matrix)
    down_matrix = in_matrix
    right_matrix = in_matrix
    if moves[0][0] and moves[0][1]:
        down_matrix.iat[moves[0][0], moves[0][1]] = True
    else:
        down_matrix = None
    if moves[1][0] and moves[1][1]:
        right_matrix.iat[moves[1][0], moves[1][1]] = True
    else:
        right_matrix = None
    route_length = moves[3][0]
    return down_matrix, right_matrix


def all_routes(start_matrix):
    matrix_df = pd.DataFrame(start_matrix)
    matrix_list = [[matrix_df]]
    route_length = 0
    i = 0
    while route_length <= 6:
        in_list = matrix_list[i]
        for matrix in in_list:
            matrix_list.append(get_route(matrix))
        i += 1
    return all_routes
