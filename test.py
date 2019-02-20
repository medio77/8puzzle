import copy
import random
class Puzzle():
    state=[]
    def __init__(self):
        #self.state=[]
        self.state.append(random.randint(0,9))
    def add_to_state(self,x):
        self.state.append(x)

if __name__ == '__main__':
    test=Puzzle()
    test2=Puzzle()
    test.add_to_state('ADDED')
    test2.state=copy.deepcopy(test.state)
    test2.add_to_state('!!!!')
    print 'test ',test.state
    print 'test2 ',test2.state
    test3=Puzzle()
    print 'test ',test.state
    print 'test2 ',test2.state
    print 'test3 ',test3.state