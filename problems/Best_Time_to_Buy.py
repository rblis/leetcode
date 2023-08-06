class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        minval = prices[0]
        for val in prices:
            minval = min(val, minval)
            ans = max(ans, val-minval)
        return ans

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))




































# def maxProfit(self, prices: [int]) -> int:
#     maxx, minn = 0, float('inf')
#     for k in range(len((prices))):
#         if prices[k] < minn:
#             minn = prices[k]
#         elif prices[k]-minn > maxx:
#             maxx = prices[k]-minn
#     return maxx


# print(maxProfit(0, [7,6,4,3,1]))