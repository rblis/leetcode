class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        last = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] > last:
                ans += prices[i] - last
                last = prices[i]
            else:
                last = prices[i]
        return ans




print(Solution().maxProfit([7,6,4,3,1]))