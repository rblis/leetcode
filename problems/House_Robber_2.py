class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2,len(nums)-1):
            dp[i] = max(nums[i]+ dp[i-2], dp[i-1])
        a = dp[-2]
        dp[2] = max(nums[2], nums[1])
        dp[1] = nums[1]
        for i in range(3, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return max(a,dp[-1])

sol = Solution()
print(sol.rob([1,2,1,1]))


'''
optimize memory by keeping a variable of the lat two houses, isntead of an array
'''