class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
        rows,cols = len(matrix), len(matrix[0])
        if rows == 1:
            if 0 in matrix[0]:
                for col in range(cols):
                    matrix[0][col] = 0
                return

        for row in range(rows-1):
            for col in range(1,cols):
                if not matrix[row][col]:
                    matrix[row][0] = 0
                    matrix[rows-1][col] = 0
        
        for row in range(rows-1):
            if not matrix[row][0]:
                for col in range(cols):
                    matrix[row][col] = 0
        for col in range(cols):
            if not matrix[rows-1][col]:
                for row in range(rows):
                    matrix[row][col] = 0
        if not matrix[0][0]:
            for col in range(cols):
                matrix[0][col] = 0
            for row in range(rows):
                matrix[row][0] = 0
        print()
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

print(Solution().setZeroes( [[1,1],[0,1],[3,1]] ))