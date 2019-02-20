import random
from anytree import Node, RenderTree


def search(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

def move_board(board, movement):  # this checks if the movement is available or not
    i_temp = 0
    j_temp = 0
    val_temp = 0
    if movement in available_moves(board):
        if movement in "balayish":
            i_temp, j_temp = search(board)
            val_temp = board[i_temp - 1][j_temp]
            board[i_temp - 1][j_temp] = 0
            board[i_temp][j_temp] = val_temp
        if movement in 'payinish':
            i_temp, j_temp = search(board)
            val_temp = board[i_temp + 1][j_temp]
            board[i_temp + 1][j_temp] = 0
            board[i_temp][j_temp] = val_temp
        if movement in 'rastish':
            i_temp, j_temp = search(board)
            val_temp = board[i_temp][j_temp + 1]
            board[i_temp][j_temp + 1] = 0
            board[i_temp][j_temp] = val_temp
        if movement in "chapish":
            i_temp, j_temp = search(board)
            val_temp = board[i_temp][j_temp - 1]
            board[i_temp][j_temp - 1] = 0
            board[i_temp][j_temp] = val_temp

    else:
        print 'error: invalid movement.'


def available_moves(board):
    avail = []
    i_zero, j_zero = search(board)
    partial_index = i_zero - 1
    if 0 <= partial_index <= 2:
        avail.append('balayish')
    partial_index = i_zero + 1
    if 0 <= partial_index <= 2:
        avail.append('payinish')
    partial_index = j_zero - 1
    if 0 <= partial_index <= 2:
        avail.append('chapish')
    partial_index = j_zero + 1
    if 0 <= partial_index <= 2:
        avail.append('rastish')
    return avail

if __name__ == '__main__':
    pickList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for i in range(len(goalState)):
        for j in range(len(goalState)):
            board[i][j] = random.choice(pickList)
            pickList.remove(board[i][j])

    print available_moves(board)



    init_node=Node('s')
    child=Node(board,parent=init_node)

    for move in available_moves(board):
        move_board(board,move)
        print board

    for pre, fill, node in RenderTree(init_node):
        print("%s%s" % (pre, node.name))
