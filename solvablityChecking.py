def is_solvable(list):
    linear_list = []
    inversion_counter = 0
    for i in list:
        for j in i:
            if j:
                linear_list.append(j)
    for i in range(len(linear_list)):
        for j in range(i, 8):
            if linear_list[i] > linear_list[j]:
                inversion_counter = inversion_counter + 1
    return inversion_counter%2==0


if __name__ == '__main__':
    board = [[5, 2, 8], [4, 1, 7], [0, 2, 6]]
    print is_solvable(board)
