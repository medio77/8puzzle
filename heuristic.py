def compute_q(q_list):
    q = 0
    base_position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                     4: (1, 0), 5: (1, 1), 6: (1, 2),
                     7: (2, 0), 8: (2, 1), 0: (2, 2)}
    for row in q_list:
        for col in row :
            if col:
                q = q + abs(base_position[col][0] - q_list.index(row)) \
                    + abs(base_position[col][1] - row.index(col))
    return q


if __name__ == '__main__':
    board = [[0, 2, 3], [4, 5, 6], [7, 8, 1]]
    # base_position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
    #                  4: (1, 0), 5: (1, 1), 6: (1, 2),
    #                  7: (2, 0), 8: (2, 1), 0: (2, 2)}
    # print base_position[2][1]
    print compute_q(board)
