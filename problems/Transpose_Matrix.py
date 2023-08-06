class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])
        if rows == cols:
            for row in range(rows):
                for col in range(row, cols):
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            return matrix
        else:
            ans = []
            for col in range(cols):
                r = []
                for row in range(rows):
                    r.append(matrix[row][col])
                ans.append(r)
            return ans

print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))