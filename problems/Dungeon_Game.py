class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = dungeon[0][0]
        for i in range(1,rows):
            dp[i][0] = dungeon[i][0] + dp[i-1][0]
        for i in range(1,cols):
            dp[0][i] = dungeon[0][i] + dp[0][i-1]
        for row in range(1,rows):
            for col in range(1,cols):
                dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + dungeon[row][col]
        
        
        
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in dp]))
        return dp[-1][-1]//rows

print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))