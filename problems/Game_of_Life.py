class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dead = []
        alive = []
        def check(row, col):
            nonlocal dead, alive
            rows, cols = len(board), len(board[0])
            count = 0
            if row > 0 and board[row-1][col]: count+=1 #North
            if col < cols-1 and board[row][col+1]: count+=1 #East
            if row < rows-1 and board[row+1][col]: count+=1 #South
            if col > 0 and board[row][col-1]: count+=1 #West
            if row > 0 and col > 0 and board[row-1][col-1]: count+=1 #North West
            if row > 0 and col < cols-1 and board[row-1][col+1]: count+=1 #North East
            if row < rows-1 and col < cols-1 and board[row+1][col+1]: count+=1 #South East
            if row < rows-1 and col > 0 and board[row+1][col-1]: count+=1 #South West

            if board[row][col] and 0 <= count < 2: dead.append([row,col])
            if board[row][col] and count > 3: dead.append([row,col])
            if not board[row][col] and count == 3: alive.append([row,col]) 
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                check(row,col)
        
        for row,col in alive:
            board[row][col] = 1
        for row,col in dead:
            board[row][col] = 0