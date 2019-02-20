import random


class Puzzle():
    # board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
   # visited=False

    def __init__(self,board):
        self.board=board
        pickList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(len(self.goalState)):
            for j in range(len(self.goalState)):
                self.board[i][j] = random.choice(pickList)
                pickList.remove(self.board[i][j])

    def print_board(self):
        for i in self.board:
            print i

    def available_moves(self):
        avail = []
        i_zero, j_zero = self.search(0)
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

    def getBoard(self):
        return self.board

    def move_board(self, movement,board):  # this checks if the movement is available or not
        i_temp = 0
        j_temp = 0
        val_temp = 0
        self.board=board
        if movement in self.available_moves():
            if movement in "balayish":
                i_temp, j_temp = self.search(0)
                val_temp = self.board[i_temp - 1][j_temp]
                self.board[i_temp - 1][j_temp] = 0
                self.board[i_temp][j_temp] = val_temp
            if movement in 'payinish':
                i_temp, j_temp = self.search(0)
                val_temp = self.board[i_temp + 1][j_temp]
                self.board[i_temp + 1][j_temp] = 0
                self.board[i_temp][j_temp] = val_temp
            if movement in 'rastish':
                i_temp, j_temp = self.search(0)
                val_temp = self.board[i_temp][j_temp + 1]
                self.board[i_temp][j_temp + 1] = 0
                self.board[i_temp][j_temp] = val_temp
            if movement in "chapish":
                i_temp, j_temp = self.search(0)
                val_temp = self.board[i_temp][j_temp - 1]
                self.board[i_temp][j_temp - 1] = 0
                self.board[i_temp][j_temp] = val_temp

        else:
            print 'error: invalid movement.'

    def search(self, item):
        for i in range(len(self.board)):
            if item in self.board[i]:
                for j in range(len(self.board[i])):
                    if self.board[i][j] == item:
                        return i, j

def none_recursive_game(puzzle):
    global visited
    visited=[]
    queue.append(puzzle)
    visited.append(puzzle)

    #---------------------------------------------------------------------
    while queue:
        temp_puzzle=queue.pop()
        # temp_puzzle=Puzzle([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        # temp_puzzle.board=very_temp_puzzle.board
        if temp_puzzle.board==temp_puzzle.goalState:
            print 'solved!'
        available_moves=temp_puzzle.available_moves()
        for move in available_moves:
                child=Puzzle([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                child.board=temp_puzzle.getBoard()
                child.move_board(move,child.board)
                #TODO: check if child is not in visited list and do next line:
                if child.board not in visited:
                    queue.append(child)
                    visited.append(child.board)
                #TODO: add child to visited list
    #----------------------------------------------------------------------




if __name__ == '__main__':

    test = Puzzle([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    queue=[]
    none_recursive_game(test)
    # test.print_board()
    # while(1):
    #     print   'available moves are: ', test.available_moves()
    #     move=raw_input()
    #     test.move_board(move)
    #     test.print_board()
