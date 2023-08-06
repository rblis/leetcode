class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        res = [0]*(len(cost))
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2,len(cost)):
            res[i] = cost[i] + min(res[i-2], res[i-1])
        
        return min(res[-2], res[-1])

sol = Solution()
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))