'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]

print(Solution().uniquePaths(3,7))






























'''
def uniquePaths(m: int, n: int) -> int:
    answer = [0]*m
    for row in range(m):#Set up matrix and base cases
        answer[row] = []
        for col in range(n):
            if row == m-1 or col == n-1:
                answer[row].append(1)
            else:
                answer[row].append(0)
    for row in range(m-2,-1, -1):
        for col in range(n-2, -1, -1):
            answer[row][col] = answer[row+1][col] + answer[row][col+1]
    
    # for row in range(m):
    #     ss = ""
    #     for col in range(n):
    #         ss += str(answer[row][col]) + " "
    #     print(ss)
        
    return answer[0][0]
print(uniquePaths(7,3))
'''