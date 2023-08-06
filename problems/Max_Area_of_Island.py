from curses import nonl


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ans, count = 0, 0
        def dfs(row, col):
            nonlocal count
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or not grid[row][col]: return
            grid[row][col] = 0
            count += 1
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                count = 0
                if grid[row][col]:
                    dfs(row,col)
                    ans = max(ans, count)
        return ans
