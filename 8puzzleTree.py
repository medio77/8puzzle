import copy
import random
from anytree import Node, RenderTree


def search(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j


def move_board(board, movement):
    i_temp = 0
    j_temp = 0
    val_temp = 0
    temp_board=copy.deepcopy(board)
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
    queue=[]
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] #this list would be changed later...
    visited=[]
    for i in range(len(goalState)):     #this is later:
        for j in range(len(goalState)):
            board[i][j] = random.choice(pickList)
            pickList.remove(board[i][j])
    print board
    print available_moves(board)

    #init_node = Node(board)
    queue.append(board)
    visited.append(board)
    while(queue):
        print len(queue)
        board=queue.pop()
        queue.append(board)
        if board== goalState:
            print "solved!"
            raw_input()
            exit(0)
        else:
            queue.pop()

        for move in available_moves(board):
            child=move_board(board, move)
            if child not in visited:
                queue.append(child)
                visited.append(child)



    print "search failed"
