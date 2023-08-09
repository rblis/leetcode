class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        size = len(grid)
        maxrow = [0]*size
        maxcol = [0]*size
        for row in range(size):
            for col in range(size):
                maxrow[row] = max(maxrow[row], grid[row][col])
                maxcol[col] = max(maxcol[col], grid[row][col])
        tot = 0
        for row in range(size):
            for col in range(size):
                if min(maxrow[row], maxcol[col]) > grid[row][col]:
                    tot += min(maxrow[row], maxcol[col]) - grid[row][col]

        return tot





grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]


Solution().maxIncreaseKeepingSkyline(grid)