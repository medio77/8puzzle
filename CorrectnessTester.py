import copy


def search(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j


def move_board(board, movement):
    i_temp = 0
    j_temp = 0
    val_temp = 0
    temp_board = copy.deepcopy(board)
    if movement in "balayish":
        i_temp, j_temp = search(temp_board)
        val_temp = temp_board[i_temp - 1][j_temp]
        temp_board[i_temp - 1][j_temp] = 0
        temp_board[i_temp][j_temp] = val_temp
    if movement in 'payinish':
        i_temp, j_temp = search(temp_board)
        val_temp = temp_board[i_temp + 1][j_temp]
        temp_board[i_temp + 1][j_temp] = 0
        temp_board[i_temp][j_temp] = val_temp
    if movement in 'rastish':
        i_temp, j_temp = search(temp_board)
        val_temp = temp_board[i_temp][j_temp + 1]
        temp_board[i_temp][j_temp + 1] = 0
        temp_board[i_temp][j_temp] = val_temp
    if movement in "chapish":
        i_temp, j_temp = search(temp_board)
        val_temp = temp_board[i_temp][j_temp - 1]
        temp_board[i_temp][j_temp - 1] = 0
        temp_board[i_temp][j_temp] = val_temp
    return temp_board


if __name__ == '__main__':
    board = [[4, 2, 1],
             [8, 7, 0],
             [5, 3, 6]]
    move_list = ['balayish', 'payinish', 'chapish', 'chapish', 'balayish', 'chapish', 'balayish', 'balayish', 'rastish',
                 'balayish', 'payinish', 'rastish', 'balayish', 'payinish', 'chapish', 'balayish', 'chapish',
                 'balayish', 'chapish', 'rastish', 'chapish', 'rastish', 'payinish', 'payinish', 'chapish', 'chapish',
                 'balayish', 'chapish', 'balayish', 'balayish', 'rastish', 'rastish', 'payinish', 'rastish', 'payinish',
                 'chapish', 'rastish', 'balayish', 'payinish']

    for move in move_list:
        board = move_board(board, move)

    print board
