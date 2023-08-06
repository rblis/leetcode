class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows, cols, squares =  [set() for _ in range(9)] , [set() for _ in range(9)], [[set() for _ in range(3)] for _ in range(3) ]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row//3][col//3]:
                        return False
                    else:
                        rows[row].add(board[row][col])
                        cols[col].add(board[row][col])
                        squares[row//3][col//3].add(board[row][col])
        return True

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

print(Solution().isValidSudoku(board))




































# def isValidSudoku() -> bool:
#     board = [["8","3",".",".","7",".",".",".","."]
#             ,["6",".",".","1","9","5",".",".","."]
#             ,[".","9","8",".",".",".",".","6","."]
#             ,["8",".",".",".","6",".",".",".","3"]
#             ,["4",".",".","8",".","3",".",".","1"]
#             ,["7",".",".",".","2",".",".",".","6"]
#             ,[".","6",".",".",".",".","2","8","."]
#             ,[".",".",".","4","1","9",".",".","5"]
#             ,[".",".",".",".","8",".",".","7","9"]]

#     cols = [set() for i in range(9)]
#     boxs = [set() for i in range(9)]
#     for row in range(9):
#         rows = set()
#         for col in range(9):
#             val = board[row][col]
#             if val != '.':
#                 if val in rows:
#                     return False
#                 else:
#                     rows.add(val)
#                 if val in cols[col]:
#                     return False
#                 else:
#                     cols[col].add(val)
#                 if 0 <= row <3 and 0 <= col < 3:
#                     if val in boxs[0]:
#                         return False
#                     else:
#                         boxs[0].add(val)
#                 elif 0 <= row < 3 and 3 <= col < 6:
#                     if val in boxs[1]:
#                         return False
#                     else:
#                         boxs[1].add(val)
#                 elif 0 <= row < 3 and 6 <= col < 9:
#                     if val in boxs[2]:
#                         return False
#                     else:
#                         boxs[2].add(val)
#                 elif 3 <= row < 6 and 0 <= col < 3:
#                     if val in boxs[3]:
#                         return False
#                     else:
#                         boxs[3].add(val)
#                 elif 3 <= row < 6 and 3 <= col < 6:
#                     if val in boxs[4]:
#                         return False
#                     else:
#                         boxs[4].add(val)
#                 elif 3 <= row < 6 and 6 <= col < 9:
#                     if val in boxs[5]:
#                         return False
#                     else:
#                         boxs[5].add(val)
#                 elif 6 <= row < 9 and 0 <= col < 3:
#                     if val in boxs[6]:
#                         return False
#                     else:
#                         boxs[6].add(val)
#                 elif 6 <= row < 9 and 3 <= col < 6:
#                     if val in boxs[7]:
#                         return False
#                     else:
#                         boxs[7].add(val)
#                 elif 6 <= row < 9 and 6 <= col < 9:
#                     if val in boxs[8]:
#                         return False
#                     else:
#                         boxs[8].add(val)
    
#     return True
# print(isValidSudoku())