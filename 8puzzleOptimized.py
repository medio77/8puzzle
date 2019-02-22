import copy
import random


# from anytree import Node, RenderTree


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


def available_moves(board_avail):
    avail = []
    #print 'board in avail :',board_avail
    i_zero, j_zero = search(board_avail)
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


def find_best_puzzle(q):
    best_p = q[0][1]
    best_board = []
    best_index = 0
    for queue_member in q:
        if queue_member[1] < best_p:
            best_p = queue_member[1]
            best_board = queue_member[0]
            best_index = q.index(queue_member)
    #print 'best board is: ',q[best_index][0]
    return q[best_index][0], best_index

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
    pickList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    index_of_parent = 1
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    queue = []
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # this list would be changed later...
    visited = []
    for i in range(len(goalState)):  # this is later:
        for j in range(len(goalState)):
            board[i][j] = random.choice(pickList)
            pickList.remove(board[i][j])
    #print board
    #print available_moves(board)

    # init_node = Node(board)
    queue.append((board, 1))
    visited.append(board)
    while queue:
        board, board_index = find_best_puzzle(queue)
        if len(queue)%1000==0:
            print len(queue)
        if board == goalState:
            print "solved!"
            raw_input()
            exit(0)
        else:
            index_of_parent = queue[board_index][1]
            queue.pop(board_index)
        #print board
        for move in available_moves(board):
            child = move_board(board, move)
            if child not in visited and is_solvable(child):
                queue.append((child, index_of_parent + 1))
                visited.append(child)

    # !!!!!!

    print "search failed"
