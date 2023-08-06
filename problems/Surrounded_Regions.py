
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(board), len(board[0])
        edges = set()
        def dfs(row,col):
            nonlocal edges, rows, cols, dirs
            if (row < 0 or row >= rows or col < 0 or col >= cols 
            or board[row][col] != 'O' or (row,col) in edges):
                return
            edges.add((row,col))
            for r,c in dirs:
                dfs(row+r,col+c)


        for row in range(rows):
            dfs(row,0)
            dfs(row,cols-1)
        for col in range(cols):
            dfs(0,col)
            dfs(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in edges and board[row][col] == 'O':
                    board[row][col] = 'X'

        return board


print(Solution().solve(
    [["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
))