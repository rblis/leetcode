class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ans = 0 
        rows, cols = len(matrix), len(matrix[0])
        def dfs(row, col):
            nonlocal ans, rows,cols
            for r in range(row, min(rows,cols)):
                for rr in range(row, r+1):
                    for c in range(col, rr):
                        if not matrix[rr][c]: return
                    print(row, col, ans)
                    ans = max(ans, rr*rr)


        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]:
                    dfs(row, col)

        return ans

print(Solution().maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))