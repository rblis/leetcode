'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        cet = set()
        def dfs(row, col, i):
            nonlocal rows, cols, cet
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[i] or (row,col) in cet:
                return False            
            cet.add((row,col))
            ans = dfs(row-1, col, i + 1) or dfs(row+1, col, i + 1) or dfs(row, col-1, i + 1) or dfs(row, col+1, i + 1)
            cet.remove((row,col))
            return ans
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True
        return False

# print(Solution().exist([["A"]],
# "A" ))
print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
"ABCB" ))
