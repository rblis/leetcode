'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1]*(n+1)
        for i in range(2,len(res)):
            res[i] = res[i-2] + res[i-1]
        return res[-1]

sol = Solution()
print(sol.climbStairs(5))