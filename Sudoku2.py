import numpy as np

class sudoku():
    def __init__(self):
        self.board  = np.zeros((9,9), dtype=int) # start with blank board
        self.__fill_cell(0)
        
    def __fill_cell(self,k):
        if k==81:
            return True      
        i = k // 9
        j = k % 9

        row = set(self.board[i,:])
        column = set(self.board[:,j])
        square = set(self.board[(i//3)*3:(1+i//3)*3,(j//3)*3:(1+j//3)*3].flatten())
        usedNumSet = row.union(column).union(square)
        # pick a number for cell (i,j) from the set of remaining available numbers        
        choices = list(set(range(1,10)).difference(usedNumSet))
        np.random.shuffle(choices)
        for choice in choices:
            self.board[i,j] = choice
            if self.__fill_cell(k+1):
                return True
        self.board[i,j] = 0
        return False

        
    def get_puzzle(self, n=81):
        mask = np.array([0]*n+[1]*(81-n),dtype=int)
        np.random.shuffle(mask)
        return mask.reshape(9,9) * self.board

    def get_solution(self):
        return self.board
            
mysudoku = sudoku()
print("puzzle:")
print(mysudoku.get_puzzle())

print("solution:")
print(mysudoku.get_solution())
