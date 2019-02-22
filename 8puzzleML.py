import copy
import random



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
    # print 'board in avail :',board_avail
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
    best_p = q[0][1] + q[0][2]
    best_board = []
    best_index = 0
    for queue_member in q:
        if queue_member[1] + queue_member[2] < best_p:
            best_p = queue_member[1]
            best_board = queue_member[0]
            best_index = q.index(queue_member)
    # print 'best board is: ',q[best_index][0]
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
    return inversion_counter % 2 == 0


def compute_q(q_list):
    q = 0
    base_position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                     4: (1, 0), 5: (1, 1), 6: (1, 2),
                     7: (2, 0), 8: (2, 1), 0: (2, 2)}
    for row in q_list:
        for col in row:
            if col:
                q = q + abs(base_position[col][0] - q_list.index(row)) \
                    + abs(base_position[col][1] - row.index(col))
    return q

def make_random_initial_puzzle(board_random):
    while (not is_solvable(board)):     #to loop until the random initial puzzle is solvable
        pickList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(len(goalState)):  # this is later:
            for j in range(len(goalState)):
                board[i][j] = random.choice(pickList)
                pickList.remove(board[i][j])


if __name__ == '__main__':
    index_of_parent = 1
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    queue = []
    board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]  # this list would be changed later...
    visited = []
    make_random_initial_puzzle(board)
    board_backup = board        #board list would be changed so i make a backup

    queue.append((board, 1, compute_q(board), []))
    visited.append(board)
    while queue:
        board, board_index = find_best_puzzle(queue)

        print len(queue)
        if board == goalState:
            print "solved!"
            # print 'moves to solve ', queue[board_index][3]  TODO: solve "moves to solve" section... i know where the problem is
            print 'initial puzzle was: ', board_backup
            exit(0)
        else:
            index_of_parent = queue[board_index][1]
            previous_move_list = copy.deepcopy(queue[board_index][3])
            queue.pop(board_index)
        # print board
        for move in available_moves(board):
            child = move_board(board, move)
            if child not in visited:
                if is_solvable(child):
                    previous_move_list.append(move)
                    queue.append((child, index_of_parent + 1, compute_q(child), previous_move_list))
                    visited.append(child)


    print "search failed"
